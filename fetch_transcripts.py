"""
Fetch YouTube transcripts for the 10 AI-powered SEO content production experts.
Uses the free youtube-transcript-api library.
Saves each transcript as a clean markdown file in research/youtube-transcripts/
"""

from youtube_transcript_api import YouTubeTranscriptApi
import os

# Each entry: (filename-safe-slug, expert name, video title, video ID, source URL)
VIDEOS = [
    ("nathan-gotch-ai-seo-saas", "Nathan Gotch",
     "Nathan Gotch on Building AI SEO SaaS: 7,000 Product Changes, No Free Trials, and the New Search Era",
     "Y88G1JbGsEE", "https://www.youtube.com/watch?v=Y88G1JbGsEE"),

    ("nathan-gotch-breaking-through-seo-ai", "Nathan Gotch",
     "Nathan Gotch's Playbook on Breaking Through SEO with AI",
     "4BSMNFNhY_E", "https://www.youtube.com/watch?v=4BSMNFNhY_E"),

    ("brian-balfour-chatgpt-growth-channel", "Brian Balfour",
     "Why ChatGPT will be the next big growth channel (and how to capitalize on it)",
     "cX4cL6B-_aU", "https://www.youtube.com/watch?v=cX4cL6B-_aU"),

    ("cyrus-shepard-google-click-data-2026", "Cyrus Shepard",
     "Google Lied About Click Data — Here's What Actually Drives Rankings in 2026",
     "rnLbyvn3L2s", "https://www.youtube.com/watch?v=rnLbyvn3L2s"),

    ("koray-tugberk-ai-agents-fortune-500", "Koray Tuğberk GÜBÜR",
     "The Complete Koray Tugberk Interview: AI Agents, Semantic SEO & Fortune 500 Secrets",
     "mSHq_HxOyTA", "https://www.youtube.com/watch?v=mSHq_HxOyTA"),

    ("ryan-law-ai-content-better-worse", "Ryan Law",
     "How AI Can Make Content Better (And Much, Much Worse): Ryan Law (Animalz)",
     "tEm4WhVc9io", "https://www.youtube.com/watch?v=tEm4WhVc9io"),

    ("tomasz-niezgoda-product-marketing-15m-arr", "Tomasz Niezgoda",
     "Product marketing to $15M ARR | Tomasz Niezgoda (Surfer)",
     "3_huJv4Xp6E", "https://www.youtube.com/watch?v=3_huJv4Xp6E"),

    ("mike-king-link-building-evolution", "Mike King",
     "Michael King of iPullRank On How Link Building Has Changed (Or Not) Over The Years",
     "x_amBRClkDo", "https://www.youtube.com/watch?v=x_amBRClkDo"),

    ("eli-schwartz-product-led-seo-ai-era", "Eli Schwartz",
     "Product-Led SEO in AI Era with Eli Schwartz",
     "x5CgYCRLgbc", "https://www.youtube.com/watch?v=x5CgYCRLgbc"),

    ("aleyda-solis-traditional-seo-vs-ai-search", "Aleyda Solis",
     "Traditional SEO vs AI Search Optimization (GEO, AEO) - #SEOFOMO TL;DR",
     "-4cu882OJ8E", "https://www.youtube.com/watch?v=-4cu882OJ8E"),
]


def fetch_and_save(slug, expert, title, video_id, url, out_dir):
    print(f"Fetching: {expert} — {title}")
    try:
        ytt_api = YouTubeTranscriptApi()
        fetched = ytt_api.fetch(video_id)
        full_text = " ".join(snippet.text for snippet in fetched)

        filename = os.path.join(out_dir, f"{slug}.md")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"**Expert:** {expert}\n\n")
            f.write(f"**Source:** {url}\n\n")
            f.write("---\n\n")
            f.write(full_text)

        print(f"  Saved -> {filename}\n")
        return True
    except Exception as e:
        print(f"  FAILED: {e}\n")
        return False


def main():
    out_dir = os.path.join("research", "youtube-transcripts")
    os.makedirs(out_dir, exist_ok=True)

    succeeded = 0
    failed = []

    for slug, expert, title, video_id, url in VIDEOS:
        ok = fetch_and_save(slug, expert, title, video_id, url, out_dir)
        if ok:
            succeeded += 1
        else:
            failed.append((expert, title, url))

    print("=" * 50)
    print(f"Done: {succeeded}/{len(VIDEOS)} transcripts saved successfully.")
    if failed:
        print("\nFailed (likely no captions available, or video is region/age-restricted):")
        for expert, title, url in failed:
            print(f"  - {expert}: {title}\n    {url}")


if __name__ == "__main__":
    main()