# Placeholder to store the tasks for now, before JSON implementation
tasks = []

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
                user_task = input("What is the task: ")
                if not user_task.strip():
                    print("Input cannot be empty or only whitespace!")
                    continue
                task = {"description": user_task.strip(), "completed": False}
                tasks.append(task)
                print("Task added successfully!")

            case 2:
                if not tasks:
                    print("No tasks found")
                    continue
                for count, task in enumerate(tasks, 1):
                    if not task["completed"]:
                        task_status = "[ ]"
                    else:
                        task_status = "[X]"
                    print(f'{count}. {task_status} {task["description"]}')

            case 3:
                if not tasks:
                    print("No tasks found")
                    continue
                print("===== YOUR TASKS =====")
                for count, task in enumerate(tasks, 1):
                    if not task["completed"]:
                        task_status = "[ ]"
                    else:
                        task_status = "[X]"
                    print(f'{count}. {task_status} {task["description"]}')
                try:
                    task_completion = int(input("Choose task to complete: "))
                    if 1 <= task_completion <= len(tasks):
                        if not tasks[task_completion - 1]["completed"]:
                            tasks[task_completion - 1]["completed"] = True
                            print("Task completed successfully!")
                        else:
                            print("This task is already completed!")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Invalid input!")

            case 4:
                if not tasks:
                    print("No tasks found")
                    continue
                print("===== YOUR TASKS =====")
                for count, task in enumerate(tasks, 1):
                    if not task["completed"]:
                        task_status = "[ ]"
                    else:
                        task_status = "[X]"
                    print(f'{count}. {task_status} {task["description"]}')
                try:
                    task_delete = int(input("Choose a task to delete: "))
                    if 1 <= task_delete <= len(tasks):
                        tasks.pop(task_delete - 1)
                        print("Task deleted successfully!")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Invalid input!")
            case 5:
                print("Goodbye!")
                break
            case _:
                print("Invalid option!")
    except ValueError:
        print("Invalid input!")