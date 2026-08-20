from __future__ import annotations
from pathlib import Path
from typing import Any

def dataset_card(record:dict[str,Any],validation:dict[str,Any])->str:
    p=record["payload"]
    return f"""# Dataset Card — {p['dataset_id']}

- Authority status: `{p['authority_status']}`
- Scientific role: {p['scientific_role']}
- Source revision: `{p['source_revision']}`
- License: {p['license']}
- Citation: {p['citation']}
- Access method: `{p['access_method']}`
- Subjects: {len(p.get('subjects',[]))}
- Sessions: {len(p.get('sessions',[]))}
- Runs: {len(p.get('runs',[]))}
- Events: {p.get('event_count',0)}
- Validation: `{validation.get('status','UNKNOWN')}`

## Mandatory limitations

- Public EEG evidence only.
- No clinical validation claim.
- No deployment or real-control claim.
- Dataset-specific label and source limitations remain controlling.
"""

def protocol_card(protocol_id:str,split_record:dict[str,Any],preprocessing_record:dict[str,Any],window_profile:dict[str,Any],leakage:dict[str,Any])->str:
    return f"""# Protocol Card — {protocol_id}

- Split record: `{split_record['record_id']}`
- Preprocessing record: `{preprocessing_record['record_id']}`
- Grouping keys: `{split_record['payload']['grouping_keys']}`
- Window duration: `{window_profile.get('duration_seconds')}` seconds
- Window stride: `{window_profile.get('stride_seconds')}` seconds
- Leakage audit: `{leakage.get('status')}`

## Mandatory limitations

- Public EEG evidence only.
- No clinical validation claim.
- No deployment or real-control claim.

## Prohibited interpretations

This protocol card does not report decoder, calibration, IHARQ, policy, stress, simulation, embodiment, clinical, or deployment performance.
"""
