import re
import calendar

from blueness import module

from bluer_journal import NAME
from bluer_journal.classes.page import JournalPage
from bluer_journal.classes.journal import journal
from bluer_journal.logger import logger


NAME = module.name(__file__, NAME)


def sync_checklist(
    verbose: bool = False,
) -> bool:
    logger.info(f"{NAME}.sync_checklist ...")

    list_of_pages = journal.list_of_pages(log=verbose)

    Home = JournalPage(
        title="Home",
        load=True,
        verbose=verbose,
    )

    logger.info("🪄")

    return True
