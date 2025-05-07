from bluer_journal.utils.sync.checklist import sync_checklist, find_todo_items


def test_sync_checklist_find_todo_items():
    dict_of_todos = find_todo_items(verbose=True)
    assert isinstance(dict_of_todos, dict)


def test_sync_checklist():
    assert sync_checklist(verbose=True)
