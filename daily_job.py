import os
import logging
from dotenv import load_dotenv
from app.scrape import OptiScraper
from app.chunker import OptiChunker
from app.upload_to_openai import OptiUploader
from app.utils import clear_folder

LOGS_DIR = "logs"
MARKDOWN_DIR = os.path.join(LOGS_DIR, "markdowns")
CHUNKS_DIR = os.path.join(LOGS_DIR, "chunks")


def run_daily_job():
    os.makedirs(LOGS_DIR, exist_ok=True)
    load_dotenv()

    # Clean previous markdowns and chunks
    clear_folder(MARKDOWN_DIR)
    clear_folder(CHUNKS_DIR)

    # 1. Scrape and delta-detect (added/updated/skipped)
    scraper = OptiScraper(MARKDOWN_DIR, num_articles=40)
    added, updated, skipped = scraper.scrape()

    # 2. Chunk by heading
    chunker = OptiChunker(MARKDOWN_DIR, CHUNKS_DIR)
    chunk_count = chunker.chunk_markdown_files() or 0

    # 3. Upload all chunks (files already deduplicated by scraper)
    uploader = OptiUploader(CHUNKS_DIR)
    uploader.upload_and_attach()

    # Return summary for logging
    return added, updated, skipped, chunk_count
