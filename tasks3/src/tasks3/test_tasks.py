from tasks3.app import next_id


def test_next_id_empty():
    assert next_id([]) == 1


def test_next_id_nonempty():
    tasks = [
        {"id": 1, "title": "a"},
        {"id": 3, "title": "b"},
        {"id": 2, "title": "c"},
    ]
    assert next_id(tasks) == 4
