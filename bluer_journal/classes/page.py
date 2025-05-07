import os
from typing import List, Dict

from bluer_objects import file

from bluer_journal.classes.journal import journal
from bluer_journal.logger import logger


class JournalPage:
    def __init__(
        self,
        title: str,
        load: bool = True,
        verbose: bool = False,
    ):
        assert title

        self.title = title
        self.verbose = verbose

        self.content: List[str] = []
        self.sections: Dict[str, List[str]] = {}

        if load:
            assert self.load()

    @property
    def filename(self) -> str:
        return os.path.join(
            journal.path,
            f"{self.title}.md",
        )

    def generate(self):
        self.content = []

        for section_name, lines in self.sections.items():
            if section_name:
                self.content.append(f"# {section_name}")

            self.content += lines

    def load(
        self,
        parse: bool = True,
    ) -> bool:
        success, self.content = file.load_text(
            self.filename,
            ignore_error=True,
            log=self.verbose,
        )
        if not success:
            return success

        if not parse:
            return True

        self.sections = {"": []}

        current_section = ""
        for line in self.content:
            if line.startswith("#"):
                current_section = line.split("#", 1)[1].strip()
                self.sections[current_section] = []
                continue

            self.sections[current_section].append(line)

        if not self.sections[""]:
            del self.sections[""]

        if self.verbose:
            logger.info(
                "loaded {} section(s) from {}: {}".format(
                    len(
                        self.sections,
                    ),
                    self.title,
                    ", ".join(self.sections.keys()),
                )
            )

        return True

    def save(
        self,
        generate: bool = True,
    ) -> bool:
        if generate:
            self.generate()

        return file.save_text(
            self.filename,
            self.content,
            log=self.verbose,
        )
