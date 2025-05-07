from bluer_journal.utils.sync.functions import sync


def test_sync():
    assert sync(
        do_checklist=True,
        verbose=True,
    )
