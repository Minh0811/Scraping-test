import os
from utils import clear_folder
from scrape import OptiScraper
from chunk import OptiChunker


def main():
    # Put the markdown files inside a logs folder and the same dir as scrape.py
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    MARKDOWN_DIR = os.path.join(SCRIPT_DIR, "logs", "markdowns")
    CHUNKS_DIR = os.path.join(SCRIPT_DIR, "logs", "chunks")

    # Clean previous log files
    clear_folder(MARKDOWN_DIR)
    clear_folder(CHUNKS_DIR)

    # Run the scraper
    scraper = OptiScraper(MARKDOWN_DIR, num_articles=40)
    scraper.scrape()

    # Run the chunker
    chunker = OptiChunker(MARKDOWN_DIR, CHUNKS_DIR)
    chunker.chunk_markdown_files()


if __name__ == "__main__":
    main()
