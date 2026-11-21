# The World in One Image — 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/135479sun-glitch/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/135479sun-glitch/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

A make.fun bounty entry: a program that sums up 20 November 2026's world news in one 1024×1024 image. It renders six verified stories — the ICJ genocide ruling on Myanmar, the first Trump–Xi–Putin summit in Shenzhen, Russia's overnight barrage on Ukraine, Anthropic's Nasdaq debut, the Houthi strike on Riyadh's tallest tower, and Russian missiles falling in Poland — as a single newspaper-style infographic.

Bounty: [`news-image-20261120`](https://make.fun/bounty/news-image-20261120) on [make.fun](https://make.fun) — $250 USDC, 50 paid places.
Deadline: 2026-11-22T00:00:00Z (2026-11-22 08:00 AWST).

## Run

```sh
python3 main.py
```

This writes `/output/entry.png` (1024×1024 PNG, ≤ 1 MiB). Pure Python + Pillow, no network, no random numbers, no timestamps — running it twice writes byte-identical output.

## What is in this repo

- `main.py` — the entry program. Reads `news.json` and renders the image.
- `news.json` — the six stories picked for 20 Nov 2026, with sources.
- `generate.py` — the earlier 1200×1800 draft generator (superseded by `main.py`).
- `news-2026-11-20.png` — the rendered 1024×1024 image, for display.
- `LICENSE` — MIT.

## Stories (checked against public reporting for 20 Nov 2026)

1. ICJ Rules Myanmar Committed Genocide (The Hague)
2. Trilateral Peace Declaration Signed in Shenzhen (Shenzhen)
3. Russia Launches Massive Strike on Ukraine (Kyiv)
4. Anthropic Debuts on Nasdaq (New York)
5. Houthi Missile Strikes Riyadh Tower (Riyadh)
6. NATO Jets Scramble After Poland Strike (Poland)

Sources: Al Jazeera, CNN, The Wall Street Journal, Kyiv Independent, NHK World, The National, Dawn, Associated Press.

## Status — NOT submitted

Draft ready for submission. Still needed before submission: upload `news-2026-11-20.png` / the rendered image (binary, not pushed by this tooling), a transcript bundle, and the wallet-signed `entry_message`. No keypair was created, nothing was submitted or claimed.
