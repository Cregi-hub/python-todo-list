from todo import display_tasks, add_task


def test_display_empty_tasks(capsys):
    new_list = []
    display_tasks(new_list)
    captured = capsys.readouterr()
    assert captured.out == "No tasks found\n"


def test_display_multiple_tasks(capsys):
    test_list = [
        {"description": "Vieraile kaverilla", "completed": False},
        {"description": "Osta uudet vaatteet", "completed": True}
    ]
    display_tasks(test_list)
    captured_out = capsys.readouterr()
    assert "1. [ ] Vieraile kaverilla\n" in captured_out.out
    assert "2. [X] Osta uudet vaatteet\n" in captured_out.out


def test_add_task(monkeypatch):
    test_list = []
    monkeypatch.setattr("builtins.input", lambda _: "Learn Python")
    monkeypatch.setattr("todo.save_tasks", lambda _: None)
    add_task(test_list)
    assert len(test_list) == 1
    assert test_list[0]["description"] == "Learn Python"
    assert test_list[0]["completed"] is False