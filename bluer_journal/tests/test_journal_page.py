from bluer_journal.classes.page import JournalPage


def test_journal_page():
    page = JournalPage(
        title="Home",
        load=True,
    )

    page.generate()

    assert page.save()
