import logging
from datetime import datetime
from daily_job import run_daily_job

LOGS_DIR = "logs"
LOG_PATH = f"{LOGS_DIR}/last_run.log"


def setup_logging():
    import sys, os

    os.makedirs(LOGS_DIR, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.FileHandler(LOG_PATH, mode="w"), logging.StreamHandler()],
    )


def main():
    setup_logging()
    logging.info(f"==== Daily job started at {datetime.now().isoformat()} ====")

    try:
        added, updated, skipped, chunk_count = run_daily_job()
        logging.info(f"Added: {added}, Updated: {updated}, Skipped: {skipped}")
        logging.info(f"Total chunks created: {chunk_count}")
        logging.info("✅ Daily job completed successfully.")
        logging.info(f"See logs/last_run.log for full artefact/logs.")
    except Exception as e:
        logging.error(f"❌ Daily job failed: {e}")

    logging.info(f"==== Job finished at {datetime.now().isoformat()} ====")


if __name__ == "__main__":
    main()
