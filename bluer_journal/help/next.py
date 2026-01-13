from typing import List

from bluer_options.terminal import show_usage, xtra


def help_next(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~open", mono=mono)

    return show_usage(
        [
            "@journal",
            "next",
            "[<title>]",
            f"[{options}]",
        ],
        "create the next page in journal.",
        mono=mono,
    )
