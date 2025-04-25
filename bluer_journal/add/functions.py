from blueness import module

from bluer_options import string
from bluer_journal import NAME
from bluer_journal.logger import logger


NAME = module.name(__file__, NAME)


def add_message(
    message: str,
    page: str = "",
    todo: bool = False,
    verbose: bool = False,
) -> bool:
    if not page:
        page = string.pretty_date(
            include_time=False,
            as_filename=True,
        )

    logger.info(
        "{}.add_message({}{}) -> {}".format(
            NAME,
            "✔️" if todo else "",
            message,
            page,
        )
    )

    logger.info("🪄")

    return True
