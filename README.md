# AI-Powered SEO Content Production — Research

This is my research project for the 100Hires growth/marketing assignment. I picked **AI-powered SEO content production for B2B SaaS** as my topic.

## What this is

I found 10 people who are actually practicing AI-powered SEO content production — not just talking about it — and collected their content (YouTube/podcast transcripts, plus some key written frameworks) so it's organized and annotated in one place. This isn't a finished playbook. It's the raw research I'd use to build one later.

## Why I picked these 10

The brief said it straight: "10 high-signal sources beat 50 generic ones." So my bar for including someone was simple — has this person actually built, run, or shipped a real content/SEO system at scale? Not just written hot takes about AI and content. I skipped a bunch of names that show up on every generic "Top AI SEO Experts" listicle because when I actually checked, they didn't meet that bar.

I also tried to avoid picking 10 people who'd basically say the same thing. I wanted range — people who'd actually disagree with each other on some things.

| Expert                  | Distinct angle                                                                            |
| ----------------------- | ----------------------------------------------------------------------------------------- |
| **Eli Schwartz**        | Product-led SEO — content that holds up even when AI summarizes it                        |
| **Kevin Indig**         | Ex-Shopify; programmatic SEO at enterprise scale, runs his own data research               |
| **Aleyda Solis**        | International/SaaS SEO; pushes back on careless AI content scaling                        |
| **Koray Tuğberk GÜBÜR** | Built his own 41-rule semantic SEO methodology and custom AI agents to run it              |
| **Nathan Gotch**        | YouTube-native AI SEO educator who also built his own AI SEO software (Rankability)        |
| **Tomasz Niezgoda**     | CMO/Co-founder of Surfer — literally runs marketing for an AI content production company   |
| **Ryan Law**            | Animalz; argues for precision over volume, a useful counterpoint to the scale-everyone-else crowd |
| **Brian Balfour**       | Reforge founder; thinks about this at the distribution/strategy level (AEO, AI as discovery) |
| **Cyrus Shepard**       | Used to be an actual Google Quality Rater; runs controlled experiments instead of guessing |
| **Mike King**           | Coined "Relevance Engineering" — by far the most technical/ML-grounded person on this list |

Full notes, links, and why I picked each one: [`research/sources.md`](research/sources.md)

## What stood out to me

Going in, I expected most "AI SEO" content to be pretty generic — the same five tips repeated by different faces. What actually surprised me was how specific some of this gets. Koray Tuğberk GÜBÜR was the clearest example — he didn't just write a listicle about using AI for content, he built an entire 41-rule semantic framework and custom AI agents to operate it. That's a different level of depth than most "AI content" advice you find online.

Finding all 10 wasn't equally easy. Some people (Mike King, Aleyda Solis) were straightforward to verify once I started looking — clear track record, real published work, easy to confirm. Others took more digging to make sure they were actual practitioners and not just people commenting on the trend from the sidelines.

## What I collected

### `research/youtube-transcripts/` — 10 transcripts

I got real video/podcast content for 9 of the 10 experts (Kevin Indig's the exception — more on that below), using the free, open-source `youtube-transcript-api` Python library. No API key, no cost. The script I used to pull these is in the repo: [`fetch_transcripts.py`](fetch_transcripts.py).

### `research/other/` — 4 deep-dives

I didn't want to force weak material into this folder just to have something for every expert. I only added something here when it genuinely added value the transcripts didn't already cover:

* **Kevin Indig** — his real expertise lives in his Growth Memo newsletter, not video. There's no equivalent YouTube content for him, so this is essential, not extra.
* **Aleyda Solis** — her full 12-step AI Search Optimization Checklist. Honestly the most useful, complete framework I found across all 10 people.
* **Mike King** — pulled together his "Relevance Engineering" framework from a few different talks and interviews.
* **Koray Tuğberk GÜBÜR** — his 41-rule methodology and his custom AI agent system, since that's the most directly relevant thing he's published.

### A note on LinkedIn

The original brief mentioned collecting LinkedIn posts. I didn't scrape LinkedIn for two reasons: LinkedIn's Terms of Service straight up prohibit scraping, and honestly — for this specific topic, the strongest people don't really live on LinkedIn. Their real work is in newsletters, blogs, and YouTube/podcasts. So I followed where their actual expertise is published instead of forcing LinkedIn coverage that wouldn't have been their best material anyway.

### A note on Kevin Indig and YouTube

Not everyone here is a video person. Rather than grab some random tangential video just to say I had 10/10 video coverage, I went with what's actually true for him — his work lives in his newsletter — and put that in `research/other/` instead.

## A few notes on how I did this

* For copyrighted material (newsletter posts, articles, frameworks), I summarized and annotated things in my own words with links back to the originals, instead of copying anything verbatim.
* YouTube transcripts are saved as-fetched (the actual captions), not paraphrased — that's just how transcripts work, different from the written-source summaries above.
* I checked every person and every source myself through web search rather than trusting existing "best of" lists at face value.

## Repo structure
research/

├── sources.md                  # All 10 experts: links, dates, why I picked them

├── youtube-transcripts/        # 10 real transcripts, one file per video

└── other/                      # 4 deep-dives on key written frameworks

fetch_transcripts.py             # Script I used to pull YouTube transcripts

## Tools I used

* **Claude** (claude.ai) — helped with research, vetting, summarizing, and figuring out repo structure
* **`youtube-transcript-api`** (Python, free/open-source) — for transcript collection
* **Git/GitHub** — committed regularly as I went, not all at the end