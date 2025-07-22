import os
from app.utils import clear_folder
from app.scrape import OptiScraper
from app.chunker import OptiChunker
from app.upload_to_openai import OptiUploader


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

    uploader = OptiUploader(CHUNKS_DIR)
    uploader.delete_all_openai_files()
    uploader.upload_and_attach()
    print(f"All operations completed successfully.")


if __name__ == "__main__":
    main()
