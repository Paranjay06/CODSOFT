import json
import os

tasks = []


def clear_screen():
    os.system("cls")


def pause():
    input("\nPress Enter to continue...")


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def load_tasks():
    global tasks

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

    except FileNotFoundError:
        tasks = []


def display_header():
    completed = sum(
        task["completed"] for task in tasks
    )

    pending = len(tasks) - completed

    print("=" * 50)
    print("          TO-DO LIST APPLICATION")
    print("=" * 50)
    print(
        f"Total Tasks: {len(tasks)} | "
        f"Pending: {pending} | "
        f"Completed: {completed}"
    )
    print("=" * 50)


def is_valid_task(task_number):
    return 1 <= task_number <= len(tasks)


def add_task():
    clear_screen()

    display_header()

    task = input("\nEnter task: ").strip()

    if task == "":
        print("\nTask cannot be empty!")
        pause()
        return

    tasks.append(
        {
            "title": task,
            "completed": False
        }
    )

    save_tasks()

    print("\nTask Added Successfully!")

    pause()


def view_tasks():

    clear_screen()

    display_header()

    if not tasks:
        print("\nNo Tasks Found!")
        pause()
        return

    print("\nYOUR TASKS")
    print("-" * 50)

    for index, task in enumerate(tasks, start=1):

        symbol = "✓" if task["completed"] else "○"

        print(
            f"{index}. [{symbol}] {task['title']}"
        )

    pause()


def update_task():

    if not tasks:
        print("\nNo Tasks Available!")
        pause()
        return

    view_tasks()

    try:

        task_number = int(
            input("\nEnter task number to update: ")
        )

        if not is_valid_task(task_number):
            print("\nInvalid Task Number!")
            pause()
            return

        new_title = input(
            "Enter new task title: "
        ).strip()

        if new_title == "":
            print("\nTask title cannot be empty!")
            pause()
            return

        tasks[task_number - 1]["title"] = new_title

        save_tasks()

        print("\nTask Updated Successfully!")

    except ValueError:
        print("\nPlease enter a valid number!")

    pause()


def complete_task():

    if not tasks:
        print("\nNo Tasks Available!")
        pause()
        return

    view_tasks()

    try:

        task_number = int(
            input("\nEnter task number to complete: ")
        )

        if not is_valid_task(task_number):
            print("\nInvalid Task Number!")
            pause()
            return

        tasks[task_number - 1]["completed"] = True

        save_tasks()

        print("\nTask Marked As Completed!")

    except ValueError:
        print("\nPlease enter a valid number!")

    pause()


def delete_task():

    if not tasks:
        print("\nNo Tasks Available!")
        pause()
        return

    view_tasks()

    try:

        task_number = int(
            input("\nEnter task number to delete: ")
        )

        if not is_valid_task(task_number):
            print("\nInvalid Task Number!")
            pause()
            return

        confirm = input(
            "\nAre you sure you want to delete this task? (y/n): "
        )

        if confirm.lower() == "y":

            tasks.pop(task_number - 1)

            save_tasks()

            print("\nTask Deleted Successfully!")

        else:
            print("\nDeletion Cancelled!")

    except ValueError:
        print("\nPlease enter a valid number!")

    pause()


# Load tasks from JSON file
load_tasks()

print(
    f"\nWelcome! {len(tasks)} task(s) loaded."
)

pause()

while True:

    clear_screen()

    display_header()

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        complete_task()

    elif choice == "5":
        delete_task()

    elif choice == "6":

        clear_screen()

        print("=" * 50)
        print("Thank You For Using To-Do List App!")
        print("=" * 50)

        break

    else:
        print("\nPlease choose a number between 1 and 6.")
        pause()