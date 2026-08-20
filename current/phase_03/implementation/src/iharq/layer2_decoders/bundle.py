from __future__ import annotations
from pathlib import Path
import zipfile,os
from .identity import sha256_file
from .writers import atomic_text,atomic_json
from .security import scan_tree,scan_zip
def checksums(root):
 r=Path(root);rows=[]
 for p in sorted(r.rglob('*')):
  if p.is_file() and p.name!='checksums.sha256':rows.append((sha256_file(p),p.relative_to(r).as_posix(),p.stat().st_size))
 atomic_text(r/'checksums.sha256',''.join(f'{h}  {x}\n' for h,x,_ in rows));return rows
def verify(root):
 r=Path(root);bad=[];missing=[];n=0
 for line in (r/'checksums.sha256').read_text().splitlines():
  if not line:continue
  h,rel=line.split('  ',1);p=r/rel;n+=1
  if not p.exists():missing.append(rel)
  elif sha256_file(p)!=h:bad.append(rel)
 return {'status':'PASS' if not bad and not missing else 'FAIL','rows':n,'missing':missing,'mismatch':bad}
def zip_bundle(root,out):
 root=Path(root);out=Path(out);checksums(root);sec=scan_tree(root)
 if sec['status']!='PASS':raise RuntimeError('SECRET_SCAN_FAILED')
 tmp=out.with_suffix('.tmp');
 with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED,allowZip64=True) as z:
  for p in sorted(root.rglob('*')):
   if p.is_file():z.write(p,(Path(root.name)/p.relative_to(root)).as_posix())
 os.replace(tmp,out)
 with zipfile.ZipFile(out) as z:bad=z.testzip();unsafe=[n for n in z.namelist() if n.startswith('/') or '..' in Path(n).parts];members=len(z.namelist())
 if bad or unsafe or scan_zip(out)['status']!='PASS':raise RuntimeError('ZIP_VALIDATION_FAILED')
 return {'status':'PASS','path':str(out),'sha256':sha256_file(out),'bytes':out.stat().st_size,'members':members,'crc':'PASS','unsafe_paths':len(unsafe)}
