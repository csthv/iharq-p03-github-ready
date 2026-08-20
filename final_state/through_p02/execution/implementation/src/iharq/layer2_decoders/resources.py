import shutil,os,platform

def snapshot(path='.'):
    t,u,f=shutil.disk_usage(path);d={'python':platform.python_version(),'cpu_count':os.cpu_count(),'disk_total_gib':t/2**30,'disk_free_gib':f/2**30,'ram_probe_status':'NOT_ATTEMPTED','cuda_probe_status':'NOT_ATTEMPTED'}
    try:
        import psutil
        v=psutil.virtual_memory();d['ram_total_gib']=v.total/2**30;d['ram_available_gib']=v.available/2**30;d['ram_probe_status']='PASS'
    except ImportError as e:
        d['ram_probe_status']='DEPENDENCY_UNAVAILABLE';d['ram_probe_error']=type(e).__name__
    except Exception as e:
        d['ram_probe_status']='PROBE_FAILED';d['ram_probe_error']=f'{type(e).__name__}:{str(e)[:160]}'
    try:
        import torch
        d['cuda_available']=bool(torch.cuda.is_available())
        if d['cuda_available']:
            d['gpu_name']=torch.cuda.get_device_name(0);d['vram_total_gib']=torch.cuda.get_device_properties(0).total_memory/2**30
        else:d['gpu_name']=None;d['vram_total_gib']=0
        d['cuda_probe_status']='PASS'
    except ImportError as e:
        d['cuda_available']=False;d['gpu_name']=None;d['vram_total_gib']=0;d['cuda_probe_status']='DEPENDENCY_UNAVAILABLE';d['cuda_probe_error']=type(e).__name__
    except Exception as e:
        d['cuda_available']=False;d['gpu_name']=None;d['vram_total_gib']=0;d['cuda_probe_status']='PROBE_FAILED';d['cuda_probe_error']=f'{type(e).__name__}:{str(e)[:160]}'
    return d

def recommended_neural_batch(d):
    if not d.get('cuda_available'):return 16
    v=float(d.get('vram_total_gib',0))
    return 64 if v>=12 else 32 if v>=8 else 16

def preflight(path,min_disk=8):
    d=snapshot(path);d['status']='PASS' if d['disk_free_gib']>=min_disk else 'RESOURCE_BLOCKED';d['disk_requirement_gib']=float(min_disk);d['recommended_neural_batch_size']=recommended_neural_batch(d);d['effective_batch_target']=64;return d
