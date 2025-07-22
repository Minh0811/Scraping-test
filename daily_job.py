# daily_job.py
import os
from app.scrape import OptiScraper
from app.chunker import OptiChunker
from app.upload_to_openai import OptiUploader

LOGS_DIR = "logs"
MARKDOWN_DIR = os.path.join(LOGS_DIR, "markdowns")
CHUNKS_DIR = os.path.join(LOGS_DIR, "chunks")


def run_daily_job():
    os.makedirs(LOGS_DIR, exist_ok=True)
    # No folder clear!
    scraper = OptiScraper(MARKDOWN_DIR, num_articles=40)
    added, updated, skipped, changed_files = scraper.scrape()

    chunk_count = 0
    if added > 0 or updated > 0:
        chunker = OptiChunker(MARKDOWN_DIR, CHUNKS_DIR)
        chunk_count = chunker.chunk_selected_files(changed_files) if changed_files else 0

        uploader = OptiUploader(CHUNKS_DIR)
        uploader.delete_all_openai_files()
        uploader.upload_and_attach()
    else:
        print("No new or updated articles. Skipping chunking and upload.")

    return added, updated, skipped, chunk_count
