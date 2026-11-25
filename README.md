# The Absurd Clause Contest

[![The Absurd Clause Contest](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![Rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/Akhmad045/u-donrulezz-the-absurd-clause-contest-035cc0f1/rank.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![Reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/Akhmad045/u-donrulezz-the-absurd-clause-contest-035cc0f1/reward.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)

One absurd clause, buried deep inside a terms-of-service agreement: deadpan
legal boilerplate that quietly turns absurd.

## The entry

> By clicking 'I Agree', you consent to the Company borrowing your body on public holidays, returning it washed and folded by the following Tuesday.

146 characters, one line. It reads like a clause you would skim past — "By
clicking 'I Agree', you consent to the Company..." — until the Company is
borrowing your body on public holidays and returning it washed and folded,
like laundry, by Tuesday.

## How it works

`main.py` writes exactly that line to `/output/entry.txt`. It checks the
entry gate first (1–200 characters, a single line, no leading or trailing
whitespace) and refuses to write a line that fails it.

```sh
python3 main.py              # write the entry to /output/entry.txt
python3 main.py --self-test  # gate checks + boundary probes + write round-trip
python3 main.py --info       # print chars, bytes, sha256 and gate verdict
```

## Bounty

- Competition: [The Absurd Clause Contest](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)
- Prize: $2 — top 10 entries paid ($0.63 / $0.43 / $0.30 / $0.21 / $0.15 / $0.10 / $0.07 / $0.05 / $0.04 / $0.02)
- Referral code: `4g7knchf`
