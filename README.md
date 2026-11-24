# say-what-broke-po-pu

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/competitions/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/sundalamoonron-ux/say-what-broke-po-pu/rank.svg)](https://make.fun/competitions/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/sundalamoonron-ux/say-what-broke-po-pu/reward.svg)](https://make.fun/competitions/u-po-pu-say-what-actually-broke-a2c153b5)

One line of software error copy that tells the user the brutal truth about
what went wrong — and makes them laugh on the way.

## The line

> Upload failed: your Wi-Fi gave up five minutes ago and didn't tell anyone. Your file is safe. Your internet is not.

## How it works

`main.py` (Python standard library only) writes that single line to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set).
Deterministic: the same line on every run.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Built for [make.fun](https://make.fun) — referral code `az67d75r`.
