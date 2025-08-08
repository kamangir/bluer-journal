from tqdm import tqdm
from typing import List, Dict, Set
import re

from blueness import module

from bluer_journal import NAME
from bluer_journal.classes.page import JournalPage
from bluer_journal.classes.journal import journal
from bluer_journal.logger import logger


NAME = module.name(__file__, NAME)

dict_of_relations: Dict[str, List[str]] = {}


def link_relations(
    page_title: str,
    verbose: bool = False,
) -> bool:
    if page_title == "Home":
        return True

    page = JournalPage(
        title=page_title,
        load=True,
        verbose=verbose,
    )
    updated_content: List[str] = []
    for line in page.content:

        if not line.startswith(": "):
            updated_content.append(line)
            continue

        keyword = line.split(": ", 1)[1]
        if not keyword:
            logger.info(f'keyword not found: "{line}"')
            return False

        if bool(re.fullmatch(r"\[\[.+?\]\]", keyword)):
            updated_content.append(line)
            continue

        updated_content.append(f": [[{keyword}]]")

    if updated_content != page.content:
        page.content = updated_content
        if not page.save(generate=False):
            return False

    set_of_relations: Set[str] = set()
    pattern = re.compile(r"\[\[([^\[\]]+)\]\]")
    for line in page.content:
        set_of_relations.update(pattern.findall(line))

    page_title_normalized = page_title.replace("-", " ")
    list_of_relations = [item.replace("-", " ") for item in list(set_of_relations)]
    dict_of_relations[page_title_normalized] = list_of_relations

    if verbose and list_of_relations:
        logger.info(
            "{} -:-> {}".format(
                page_title_normalized,
                ", ".join(list_of_relations),
            )
        )

    return True


def sync_relations(
    verbose: bool = False,
) -> bool:
    logger.info(f"{NAME}.sync_relations ...")

    dict_of_relations = {}

    list_of_pages = journal.list_of_pages(log=verbose)
    for page_title in tqdm(list_of_pages):
        if not link_relations(
            page_title=page_title,
            verbose=verbose,
        ):
            return False

    return True
