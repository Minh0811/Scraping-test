import os
import re
from dotenv import load_dotenv
import requests
from markdownify import markdownify as md

class OptiScraper:
    def __init__(self, output_dir, num_articles=40):
        # load variables from .env
        load_dotenv()
        self.API_URL = os.getenv("API_URL")
        self.OUTPUT_DIR = output_dir
        self.NUM_ARTICLES = num_articles

    def slugify(self, text):
        return re.sub(r'[^a-zA-Z0-9-]+', '-', text.lower()).strip('-')

    def fetch_articles(self):
        articles = []
        url = self.API_URL

        while url and len(articles) < self.NUM_ARTICLES:
            print(f"Fetching: {url}")
            r = requests.get(url)
            r.raise_for_status()
            data = r.json()
            articles.extend(data.get("articles", []))
            url = data.get("next_page")

        return articles[:self.NUM_ARTICLES]

    def scrape(self):
        os.makedirs(self.OUTPUT_DIR, exist_ok=True)
        articles = self.fetch_articles()

        for art in articles:
            title = art.get("title", "untitled")
            html_body = art.get("body", "")
            markdown_body = md(html_body)
            slug = self.slugify(title)
            filename = f"{slug}.md"
            file_path = os.path.join(self.OUTPUT_DIR, filename)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# {title}\n\n{markdown_body}")
            print(f"Saved: {file_path}")

        print(f"Done. {len(articles)} articles saved to {self.OUTPUT_DIR}/")
