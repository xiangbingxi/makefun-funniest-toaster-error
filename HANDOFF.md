# Handoff — The Funniest Toaster Error Message

Competition: https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd
Repo name: makefun-funniest-toaster-error

## Entry (verbatim, as given by the user)

```
ERROR 409: Bread ejected successfully; toast remains a matter of opinion.
```

- Characters: 73 (limit 120)
- Bytes: 73 (pure ASCII, UTF-8)
- No trailing newline.

## How it works

`main.py` writes the entry string to `/output/entry.txt` (UTF-8, no
trailing newline). It reads no external files and uses no network.
It was written in two passes: v1 wrote the file plainly; v2 added a
length guard (1–120 chars) and reads `/output/entry.txt` back after
writing, exiting with an error if the bytes differ from the entry
string by even one byte.

## Verification

- Ran `main.py` twice (final version): both exits 0, outputs `cmp`
  byte-identical.
- `entry.txt` vs the entry string: exact match (73 bytes / 73 chars,
  no trailing newline).
- sha256 of `entry.txt`:
  `b04021a6a97dc3c47d3b3b7c6898a4674e9694ffad58e44068d0a27541acc37a`
- Same sha256 from the v1 run and the v2 runs: the two versions agree.
- `prompt.txt` is 73 bytes, the entry on a single line.
- `LICENSE` is MIT and contains `SPDX-License-Identifier: MIT`.
- `README.md` carries the competition link and all three official
  make.fun badges.
- `.makefun/owner.json` holds wallet
  `6t8k8dD19c2zDMiZ1VNsbRDWaSNSedmQQB6A15hy3XFx`.

## Status

Files complete. Not submitted, no GitHub repo created, no bundle made —
those steps are for the parent agent.
