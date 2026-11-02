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
                print(tasks)
            case 3:
                print("Feature not implemented yet")
            case 4:
                print("Feature not implemented yet")
            case 5:
                print("Goodbye!")
                break
            case _:
                print("Invalid option!")
    except ValueError:
        print("Invalid input!")