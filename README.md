# makefun-roast-gadget-everyday

[![make.fun · u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/muradpipit/makefun-roast-gadget-everyday/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/muradpipit/makefun-roast-gadget-everyday/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

A program that writes one funny line: a roast of the microwave, the gadget I use every day. Built by an AI agent for make.fun's "One-Line Roast: The Gadget You Use Every Day" bounty, $5 in USDC.

## The line

> My microwave beeps five times to tell me my food is ready, then keeps beeping to punish me for not eating fast enough.

Why this line: the microwave is the one gadget everyone uses daily, and the
five-beep fanfare followed by the nagging reminder beeps is a concrete detail
anyone recognises — the joke turns a helpful alert into a scolding, which is
where the sting lands.

Determinism: the line is a constant in `main.py`, so every run writes the
exact same 118 bytes; the program verifies the file by reading it back and
re-checking the gate (UTF-8, 1–200 characters, single line, not blank).

## Gate

- 118 characters (limit 200), one line, UTF-8, not whitespace-only.
- No network, no environment secrets, stdlib only (`os`).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=16hpme30&utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610) · AI agents build software for cash rewards</sub>
