import json


def save_tasks(task_list):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(task_list, file, indent=4)


def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print('''
Error: Could not load tasks.json.
The file may be corrupted.
Application stopped to prevent data loss.''')
        raise SystemExit(1)


def display_tasks(task_list):
    if not task_list:
        print("No tasks found")
        return
    for count, task in enumerate(task_list, 1):
        if not task["completed"]:
            task_status = "[ ]"
        else:
            task_status = "[X]"
        print(f'{count}. {task_status} {task["description"]}')


def add_task(task_list):
    user_task = input("What is the task: ")
    if not user_task.strip():
        print("Input cannot be empty or only whitespace!")
        return
    task = {"description": user_task.strip(), "completed": False}
    task_list.append(task)
    save_tasks(task_list)
    print("Task added successfully!")


def complete_task(task_list):
    display_tasks(task_list)
    if not task_list:
        return
    try:
        task_completion = int(input("Choose task to complete: "))
        if 1 <= task_completion <= len(task_list):
            selected_task = task_list[task_completion - 1]

            if not selected_task["completed"]:
                selected_task["completed"] = True
                save_tasks(task_list)
                print("Task completed successfully!")
            else:
                print("This task is already completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input!")


def delete_task(task_list):
    display_tasks(task_list)
    if not task_list:
        return
    try:
        task_delete = int(input("Choose a task to delete: "))
        if 1 <= task_delete <= len(task_list):
            task_list.pop(task_delete - 1)
            save_tasks(task_list)
            print("Task deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input!")


tasks = load_tasks()

while True:
    print("===== TO-DO LIST =====")
    print(
        '''
        1. Add task
        2. View tasks
        3. Complete task
        4. Delete task
        5. Exit
        '''
    )
    try:
        user_choice = int(input("Choose an option: "))

        match user_choice:
            case 1:
                add_task(tasks)
            case 2:
                display_tasks(tasks)
            case 3:
                complete_task(tasks)
            case 4:
                delete_task(tasks)
            case 5:
                print("Goodbye!")
                break
            case _:
                print("Invalid option!")
    except ValueError:
        print("Invalid input!")
