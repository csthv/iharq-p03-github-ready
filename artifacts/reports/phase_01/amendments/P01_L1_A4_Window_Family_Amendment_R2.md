# P01/L1 A4 Window-Family Additive Amendment R2

## Status

`DATA_READY_PROTOCOL_SYNC_REQUIRED`

## Unchanged official core

The verified core Dataset remains immutable:

- Handle: `csthv999z/iharq-p01-l1-derived-windows-d03f0a7c869d-20260806222242-68a91473`
- Provider version: `2`
- Manifest SHA-256:
  `dc21f418e9a1add62adb346f627d5d729735a5f1ecaa1d771f6fa5cfede627e1`
- Official core window: cue +0.5 s to +3.5 s.

## Additive A4 data substrate

A separate Dataset stores one lossless cue +0.0 s to +3.5 s
tensor for every included source event. It also registers three
exact same-event 2-second views:

1. +0.0 s to +2.0 s
2. +0.75 s to +2.75 s
3. +1.5 s to +3.5 s

The views reference slices of the matched 3.5-second tensor; their
overlapping bytes are not duplicated.

## Governance boundary

This execution makes the data substrate available to Layer 2.
Confirmatory A4 claims require the exact profile and group
configuration to be synchronized into Protocol v1.0 and the
applicable Build Book. Until then, the data are valid for
implementation readiness and diagnostic execution, not silent
confirmatory promotion.

## Dataset

- Handle: `csthv999z/iharq-p01-l1-a4-d03f0a7c-9a7c6108`
- Provider version: `1`
- A4 config ID: `4cd080393345e8aa215280fc51736b5b6fb42693da8120c259e5de7316427518`
