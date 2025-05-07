from typing import List

from bluer_options.terminal import show_usage, xtra
from bluer_ai.help.generic import help_functions as generic_help_functions

from bluer_journal import ALIAS
from bluer_journal.help.add import help_add
from bluer_journal.help.git import help_functions as help_git
from bluer_journal.help.open import help_open


def help_sync(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~checklist,dryrun,~push", mono=mono)

    return show_usage(
        [
            "@journal",
            "sync",
            f"[{options}]",
        ],
        "sync journal.",
        mono=mono,
    )


help_functions = generic_help_functions(plugin_name=ALIAS)


help_functions.update(
    {
        "add": help_add,
        "git": help_git,
        "open": help_open,
        "sync": help_sync,
    }
)
