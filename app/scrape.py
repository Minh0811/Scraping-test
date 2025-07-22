import os
import re
from dotenv import load_dotenv
import requests
from markdownify import markdownify as md
import json
import hashlib
from datetime import datetime


class OptiScraper:
    def __init__(self, output_dir, num_articles=None):
        # load variables from .env
        load_dotenv()
        self.API_URL = os.getenv("API_URL")
        self.OUTPUT_DIR = output_dir
        self.NUM_ARTICLES = num_articles

    def slugify(self, text):
        return re.sub(r"[^a-zA-Z0-9-]+", "-", text.lower()).strip("-")

    def fetch_articles(self):
        articles = []
        url = self.API_URL

        while url and (self.NUM_ARTICLES is None or len(articles) < self.NUM_ARTICLES):
            print(f"Fetching: {url}")
            r = requests.get(url)
            r.raise_for_status()
            data = r.json()
            articles.extend(data.get("articles", []))
            url = data.get("next_page")

        return articles[: self.NUM_ARTICLES]


    def scrape(self):
        os.makedirs(self.OUTPUT_DIR, exist_ok=True)
        # Metadata for delta detection
        metadata_path = os.path.join(self.OUTPUT_DIR, "..", "metadata.json")
        if os.path.exists(metadata_path):
            with open(metadata_path, "r", encoding="utf-8") as f:
                prev_metadata = json.load(f)
        else:
            prev_metadata = {}

        articles = self.fetch_articles() or []
        added, updated, skipped = 0, 0, 0
        new_metadata = {}

        for art in articles:
            article_id = str(art.get("id", ""))
            title = art.get("title", "untitled")
            html_body = art.get("body", "")
            markdown_body = md(html_body)
            slug = self.slugify(title)
            filename = f"{slug}.md"
            file_path = os.path.join(self.OUTPUT_DIR, filename)
            content_hash = hashlib.md5(markdown_body.encode("utf-8")).hexdigest()
            last_modified = art.get("updated_at") or art.get("created_at") or ""

            old = prev_metadata.get(article_id)
            if old is None:
                added += 1
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"# {title}\n\n{markdown_body}")
            elif old["hash"] != content_hash or old["last_modified"] != last_modified:
                updated += 1
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"# {title}\n\n{markdown_body}")
            else:
                skipped += 1

            new_metadata[article_id] = {
                "hash": content_hash,
                "last_modified": last_modified,
                "title": title,
                "filename": filename,
            }

        # Save new metadata
        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(new_metadata, f, indent=2)

        print(f"Added: {added}, Updated: {updated}, Skipped: {skipped}")
        return added, updated, skipped
