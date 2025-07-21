import os
import re
import requests
from markdownify import markdownify as md

# Config
API_URL = "https://support.optisigns.com/api/v2/help_center/en-us/articles.json"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "optisigns_markdown")
NUM_ARTICLES = 40

os.makedirs(OUTPUT_DIR, exist_ok=True)
articles = []
url = API_URL

# Fetch articles (paginate if needed)
while url and len(articles) < NUM_ARTICLES:
    print(f"Fetching: {url}")
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    #print(f"response: {data}")
    articles.extend(data.get("articles", []))
    url = data.get("next_page")

# Limit to NUM_ARTICLES
articles = articles[:NUM_ARTICLES]

def slugify(text):
    return re.sub(r'[^a-zA-Z0-9-]+', '-', text.lower()).strip('-')

# Process and save
for art in articles:
    title = art.get("title", "untitled")
    html_body = art.get("body", "")
    markdown_body = md(html_body)
    slug = slugify(title)
    filename = f"{slug}.md"
    file_path = os.path.join(OUTPUT_DIR, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{markdown_body}")
    print(f"Saved: {file_path}")

print(f"Done. {len(articles)} articles saved to {OUTPUT_DIR}/")
