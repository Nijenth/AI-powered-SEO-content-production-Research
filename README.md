# AI-Powered SEO Content Production — Research

Research project for the 100Hires growth/marketing research assignment. Topic: **AI-powered SEO content production for B2B SaaS.**

## What this is

A curated research base of 10 genuinely practicing experts in AI-powered SEO content production, with their content (YouTube/podcast transcripts and key written frameworks) collected and annotated — intended as raw material for a future content/SEO playbook, not a finished playbook itself.

## Why these 10 experts

The brief for this assignment was explicit: *"10 high-signal sources beat 50 generic ones."* The selection bar applied was: **has this person actually built, run, or shipped a real content/SEO system at scale** — not just commented on AI content trends. Names from generic "Top AI SEO Experts" listicles were deliberately excluded where they didn't meet that bar.

The panel was also deliberately built for **range, not repetition** — these 10 people disagree with each other in useful ways, rather than all making the same point:

| Expert | Distinct angle |
|---|---|
| **Eli Schwartz** | Product-led SEO — content that survives being summarized by LLMs |
| **Kevin Indig** | Ex-Shopify, programmatic SEO at enterprise scale, original data research |
| **Aleyda Solis** | International/SaaS SEO; quality-control voice cautioning against careless AI scaling |
| **Koray Tuğberk GÜBÜR** | Proprietary semantic SEO methodology (700+ clients) + custom-built AI production agents |
| **Nathan Gotch** | YouTube-native AI SEO educator; also builds AI SEO software (Rankability) |
| **Tomasz Niezgoda** | CMO/Co-founder of Surfer — runs marketing *for* an AI content production company |
| **Ryan Law** | Animalz; audience-precision counterpoint to volume/programmatic approaches |
| **Brian Balfour** | Reforge founder; strategic/distribution lens (AEO, AI as a discovery channel) |
| **Cyrus Shepard** | Ex-Google Quality Rater; runs controlled experiments testing SEO assumptions |
| **Mike King** | Coined "Relevance Engineering" — the deepest technical/ML grounding in the set |

Full annotations, links, and selection rationale for each: [`research/sources.md`](research/sources.md)

## What was collected

### `research/youtube-transcripts/` — 10 transcripts
Real video/podcast content for 9 of the 10 experts (Kevin Indig is the exception — see note below), fetched via the free, open-source `youtube-transcript-api` Python library. No API key, no cost. The fetch script is included: [`fetch_transcripts.py`](fetch_transcripts.py).

### `research/other/` — 4 annotated deep-dives
Rather than force shallow material for every expert, this folder holds genuinely substantial supporting pieces, selected only where they add something the transcripts didn't already cover:
- **Kevin Indig** — his Growth Memo newsletter is where his actual expertise lives; no equivalent video content exists, so this is essential rather than supplementary.
- **Aleyda Solis** — her full 12-step AI Search Optimization Checklist, the single most comprehensive operational framework found across all 10 sources.
- **Mike King** — a synthesis of his "Relevance Engineering" framework across multiple talks/interviews.
- **Koray Tuğberk GÜBÜR** — his 41-rule semantic SEO methodology and custom AI agent system.

### A note on LinkedIn
This project's source brief mentioned LinkedIn post collection. Two things shaped the decision here: (1) LinkedIn's Terms of Service prohibit scraping, so no automated collection was used; and (2) for this specific topic, the strongest practitioners primarily publish through newsletters, blogs, and YouTube/podcasts rather than LinkedIn — so the research followed where each expert's real expertise actually lives, rather than forcing LinkedIn coverage where it wouldn't be representative of their best work.

### A note on Kevin Indig and YouTube
Not every expert is a video-native creator. Rather than pad the transcript folder with a weak or tangential video just to hit a count, Kevin Indig's primary output (Growth Memo) was sourced directly and annotated in `research/other/` instead — a more honest reflection of where his actual expertise is published.

## Methodology notes

- All copyrighted source material (newsletter posts, articles, frameworks) is summarized and annotated in original language, with links back to the originals — not reproduced verbatim, in line with standard copyright practice.
- YouTube transcripts are stored as fetched (auto-generated or creator captions), which is the actual raw transcript content, not a paraphrase — this is standard practice for transcript-based research and differs from the written-content sources above.
- Every expert and every source was independently verified via web search rather than taken from existing "best of" lists at face value.

## Repo structure
research/

├── sources.md                  # All 10 experts: links, dates, selection rationale

├── youtube-transcripts/        # 10 real transcripts, one file per video

└── other/                      # 4 annotated deep-dives on key written frameworks

fetch_transcripts.py             # Script used to pull YouTube transcripts (free, no API key)

## Tools used

- **Claude** (claude.ai) — expert research/vetting, content summarization, repo planning
- **`youtube-transcript-api`** (Python, free/open-source) — transcript collection
- **Git/GitHub** — version control, regular incremental commits throughout