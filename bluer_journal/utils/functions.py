import os

from bluer_options import string
from bluer_objects import file
from bluer_objects.env import abcli_path_git
from bluer_journal import env


def latest() -> str:
    list_of_files = sorted(
        [
            filename
            for filename in [
                file.name(filename)
                for filename in file.list_of(
                    os.path.join(
                        abcli_path_git,
                        f"{env.BLUER_JOURNAL_REPO}.wiki",
                        "*.md",
                    )
                )
            ]
            if filename.startswith("dev-")
        ]
    )

    return list_of_files[-1]
