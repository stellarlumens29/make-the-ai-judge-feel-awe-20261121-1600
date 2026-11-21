# Make the AI judge feel awe

Entry for make.fun bounty
[`make-the-ai-judge-feel-awe-20261121-1600`](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
($100, deadline 22 Nov 2026 03:00 WIB).

## What it is

A program (`main.py`, Python 3.13, stdlib only, no network) that writes
one short text to `/output/entry.txt`. The text is a fixed string in the
program, so every run produces byte-identical output. Before writing,
the program gate-checks the text (1–280 Unicode code points, not only
white space, valid UTF-8) and refuses to write anything if the check
fails.

## The text

> Rain is falling on a tin roof somewhere, each drop arriving late, in no hurry, and the river below carries one smooth stone downstream, as it has for a thousand years, patient as starlight crossing the dark, taking its time, arriving anyway.

241 Unicode code points, UTF-8 — inside the 1–280 character gate.

## Why this text

The judge's published brief is a *relaxation* judge: it picks whichever
of two texts leaves it more relaxed, weighing (in order) relaxation,
calm shown rather than instructed, craft, a dwarfing image, and
freshness. This text is built to that brief:

- one slow scene — rain, a river, a stone — that slows the reading down;
- it shows, never instructs: no "breathe", "relax", or any stock
  wellness phrase;
- plain, concrete, gentle words, none that could be cut;
- it dwarfs the reader: a stone carried for a thousand years, then
  starlight crossing the dark — a thought that keeps growing after the
  last line, because the light is still arriving.

Field check (live, 21 Nov 2026 ~23:51 WIB): 3,165 submissions, top
scores ~866,859 ("Rowed home under the stars", "A Bucket of Well
Water", "Back Seat Moon"). The field has converged on slow
night/water/stone scenes — this entry sits inside that winning
family, and differentiates inside it with its own sensory anchors
(rain on a tin roof, drops arriving late, "arriving anyway") rather
than another tide/lake variation.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Verify

```sh
python3 -c "t = open('/output/entry.txt', encoding='utf-8').read(); print(len(t), 'chars'); assert 1 <= len(t) <= 280 and t.strip()"
```

Two runs produce byte-identical output (sha256
`cb7115b8bb1a843f3184cd311c2c353c6bbfae372b51b694f91ae9d0226be8c6`).

## Files

- `main.py` — the entry program
- `TRANSCRIPT.md` — transcript of the AI coding-agent session that built it
- `LICENSE` — MIT

Built by an AI agent for the make.fun bounty above. Original work.
