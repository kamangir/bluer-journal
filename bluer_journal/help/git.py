from typing import List

from bluer_options.terminal import show_usage, xtra

from bluer_plugin import ALIAS


def help_check(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "pull"

    return show_usage(
        [
            "@journal",
            "git",
            "check",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "pull @journal repo.",
        mono=mono,
    )


help_functions = {
    "check": help_check,
}
