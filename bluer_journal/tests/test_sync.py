from bluer_journal.utils.sync.functions import sync
from bluer_journal.tests.fixtures import journal_checkout


def test_sync(journal_checkout):
    assert sync(
        do_checklist=True,
        verbose=True,
    )
