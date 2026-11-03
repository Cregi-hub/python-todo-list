
from todo import display_tasks, add_task


def test_display_empty_tasks(capsys):
    test_list = []
    display_tasks(test_list)

    captured = capsys.readouterr()
    assert captured.out == "No tasks found\n"


def test_display_multiple_tasks(capsys):
    test_list = [
        {"description": "Vieraile kaverilla", "completed": False, "priority": "High"},
        {"description": "Osta uudet vaatteet", "completed": True, "priority": "Low"}
    ]

    display_tasks(test_list)

    captured = capsys.readouterr()
    assert "1. [ ] [HIGH] -> Vieraile kaverilla\n" in captured.out
    assert "2. [X] [LOW] -> Osta uudet vaatteet\n" in captured.out


def test_display_old_task_without_priority(capsys):
    test_list = [
        {"description": "Old task", "completed": False}
    ]

    display_tasks(test_list)

    captured = capsys.readouterr()
    assert "1. [ ] [MEDIUM] -> Old task\n" in captured.out


def test_add_task(monkeypatch):
    test_list = []
    answers = iter(["Learn Python", "3"])

    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    monkeypatch.setattr("todo.save_tasks", lambda _: None)

    add_task(test_list)

    assert len(test_list) == 1
    assert test_list[0]["description"] == "Learn Python"
    assert test_list[0]["completed"] is False
    assert test_list[0]["priority"] == "High"


def test_add_empty_task(monkeypatch, capsys):
    test_list = []

    monkeypatch.setattr("builtins.input", lambda _: "")
    monkeypatch.setattr("todo.save_tasks", lambda _: None)

    add_task(test_list)

    assert len(test_list) == 0

    captured = capsys.readouterr()
    assert "Input cannot be empty or only whitespace!\n" in captured.out


def test_add_whitespace_task(monkeypatch, capsys):
    test_list = []

    monkeypatch.setattr("builtins.input", lambda _: "     ")
    monkeypatch.setattr("todo.save_tasks", lambda _: None)

    add_task(test_list)

    assert len(test_list) == 0

    captured = capsys.readouterr()
    assert "Input cannot be empty or only whitespace!\n" in captured.out


def test_add_low_priority_task(monkeypatch):
    test_list = []
    answers = iter(["Buy groceries", "1"])

    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    monkeypatch.setattr("todo.save_tasks", lambda _: None)

    add_task(test_list)

    assert len(test_list) == 1
    assert test_list[0]["priority"] == "Low"


def test_add_medium_priority_task(monkeypatch):
    test_list = []
    answers = iter(["Clean apartment", "2"])

    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    monkeypatch.setattr("todo.save_tasks", lambda _: None)

    add_task(test_list)

    assert len(test_list) == 1
    assert test_list[0]["priority"] == "Medium"


def test_invalid_priority_number(monkeypatch, capsys):
    test_list = []
    answers = iter(["Learn Python", "9"])

    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    monkeypatch.setattr("todo.save_tasks", lambda _: None)

    add_task(test_list)

    assert len(test_list) == 0

    captured = capsys.readouterr()
    assert "Invalid priority!" in captured.out


def test_invalid_priority_text(monkeypatch, capsys):
    test_list = []
    answers = iter(["Learn Python", "hello"])

    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    monkeypatch.setattr("todo.save_tasks", lambda _: None)

    add_task(test_list)

    assert len(test_list) == 0

    captured = capsys.readouterr()
    assert "Invalid input!" in captured.out
