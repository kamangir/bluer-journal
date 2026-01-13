from bluer_journal.utils.latest import latest
from bluer_journal.logger import logger


def next() -> str:
    latest_page = latest()
    logger.info(f"latest: {latest_page}")

    logger.info("🪄")

    return "TBA"
