import re
import calendar

from blueness import module

from bluer_journal import NAME
from bluer_journal.classes.page import JournalPage
from bluer_journal.logger import logger


NAME = module.name(__file__, NAME)


def sync_checklist(
    verbose: bool = False,
) -> bool:
    logger.info(f"{NAME}.sync_checklist ...")

    logger.info("🪄")

    return True
