from tqdm import tqdm
from typing import Dict

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

    dict_of_todos: Dict[str, str] = {}
    for page_title in tqdm(list_of_pages):
        if page_title == "Home":
            continue

        page = JournalPage(
            title=page_title,
            load=True,
            verbose=verbose,
        )

        for todo_item in page.list_of_todos():
            dict_of_todos[todo_item] = page_title

    dict_of_todos = dict(sorted(dict_of_todos.items()))

    logger.info(f"{len(dict_of_todos)} todo(s).")
    for index, (todo_item, page_title) in enumerate(dict_of_todos.items()):
        logger.info(f"#{index+1: 3d} - {todo_item} ({page_title})")

    return True
