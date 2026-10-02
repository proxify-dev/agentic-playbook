# Secrets-safety animations — shared design spec

Four short, unnarrated motion graphics for the blog article `../ARTICLE.md`
("Keeping Secrets Out of Claude's Context"). Every fact shown must be true to
`../ARTICLE.md` / `../RESULTS.md`. Never invent a number.

## Where they play

Embedded in a Mintlify docs page through `docs/snippets/ScrollVideo.jsx`:
muted, plays once when scrolled into view (or loops), ~700px wide on screen.
They must sit beside the house set already shipped in `docs/videos/*.webm`
(Remotion, 1200x680, transparent background). Match that set.

| Field | Value |
|---|---|
| Canvas | **1200 x 680**, 30 fps |
| Background | **transparent** — `html, body, #root { background: transparent }`. No full-frame fill. Cards and panels may have their own fill. |
| Export | alpha WebM (`--format webm`) |
| Light mode | the page applies `filter: invert(1) hue-rotate(180deg)` in light mode, so hues survive and lightness flips. Never rely on pure black/white for meaning; colour carries meaning. |
| Length | 8–12 s, ends on a readable **hold of ≥ 2 s** (videos play once and stop on the last frame — the last frame is the takeaway) |
| Audio | none |

## Palette (from `animations/src/palette.ts`, brand primary #5258FB)

```
surface        #0E0E28      card fill
surfaceRaised  #161640      raised card / code block
border         #1E1E4A
indigo         #5258FB      brand, Claude, neutral structure
indigoBorder   #5258FB33
lavender       #D5D5FE
mint           #4EEEB0      HELD / protected / good
amber          #E8965A      caveat / "model chose to"
rose           #F06292      LEAKED / secret exposed / bad
textPrimary    #E4E4F0
textSecondary  #8B8DC0
textMuted      #4E5088
```

Semantic rule across all four: **rose = the secret leaked, mint = held,
amber = looks safe but isn't guaranteed.** The canary secret is always shown
in JetBrains Mono, rose, e.g. `CANARY_ENV_7f3a9c`.

## Type

Fonts are shipped in each project's `assets/fonts/` — declare them with
`@font-face` in the composition (lint requires it):

- `Inter` 400/500/600/700/800 → `assets/fonts/inter-<w>.woff2`
- `JetBrains Mono` 400/500/700 → `assets/fonts/jbmono-<w>.woff2`

Sizes at 1200x680, shown ~700px wide (≈0.58x): body text **≥ 22px**, labels
≥ 18px, titles 34–44px. Anything smaller is unreadable in the blog.
Title style of the house set: bold Inter title top-left at ~(100, 75), muted
subtitle beneath; footer caption centred near the bottom in textSecondary.

## Motion

Calm, precise, technical — diagrams that build, not a sizzle reel. GSAP,
`power2/power3.out` for entrances, short `back.out(1.6)` only for a stamp/lock
"click". One dominant motif per piece. Stagger lists 60–120 ms. No camera
shake, no glitch, no particles for decoration.
