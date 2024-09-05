import json
import os
from datetime import datetime

tasks = []

def add_task(title, due_date):
    tasks.append({"title": title, "due_date": due_date, "completed": False})

def mark_task_complete(task_number, complete=True):
    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = complete

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
   
    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Incomplete"
        print(f"{i + 1}. {task['title']} (Due: {task['due_date']}) - {status}")

def view_completed_tasks():
    if not tasks:
        print("No tasks available.")
        return

    task_number = 1
    for task in tasks:
        if task["completed"]:
            print(f"{task_number}. {task['title']} (Due: {task['due_date']}) - Completed")
            task_number += 1
   
    if task_number == 1:
        print("No completed tasks.")

def view_incomplete_tasks():
    if not tasks:
        print("No tasks available.")
        return

    task_number = 1
    for task in tasks:
        if not task["completed"]:
            print(f"{task_number}. {task['title']} (Due: {task['due_date']}) - Incomplete")
            task_number += 1

    if task_number == 1:
        print("No incomplete tasks.")

def remove_all_tasks():
    tasks.clear()
    print("All tasks have been removed.")

def save_tasks_to_file(filename="Tasks.json"):
    if filename is None:
        filename = os.path.join(os.path.expanduser("~"), "Documents", "Python", "tasks.json")
   
    try:
        with open(filename, "w") as file:
            json.dump(tasks, file, indent=4, default=str)
        print(f"Tasks saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving tasks: {e}")
       
def load_tasks_from_file(filename="tasks.json"):
    global tasks
    if filename is None:
        filename = os.path.join(os.path.expanduser("~"), "Documents", "Python", "tasks.json")
    if not os.path.exists(filename):
        print(f"No file found with the name {filename}. Starting with an empty task list.")
        tasks = []
        return
   
    try:
        with open(filename, "r") as file:
            loaded_tasks = json.load(file)
        for task in loaded_tasks:
            task["due_date"] = datetime.strptime(task["due_date"], "%Y-%m-%d")
       
        tasks = loaded_tasks
        print(f"Tasks loaded from {filename}.")
       
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}. Starting with an empty task list.")
        tasks = []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        tasks = []


def main():
    load_tasks_from_file()  # Attempt to load tasks from file

    while True:
        print("\nTo-Do List:")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. View completed tasks")
        print("4. View incomplete tasks")
        print("5. Mark task as complete")
        print("6. Mark task as incomplete")
        print("7. Remove all tasks")
        print("8. Save tasks to file")
        print("9. Load tasks from file")
        print("10. Exit")
       
        choice = input("Choose an option: ")
       
        if choice == "1":
            title = input("Enter the task title: ")
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            add_task(title, due_date)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_completed_tasks()  
        elif choice == "4":
            view_incomplete_tasks()
        elif choice == "5":
            task_number = int(input("Enter the task number to mark as complete: ")) - 1
            mark_task_complete(task_number, complete=True)
        elif choice == "6":
            task_number = int(input("Enter the task number to mark as incomplete: ")) - 1
            mark_task_complete(task_number, complete=False)
        elif choice == "7":
            remove_all_tasks()
        elif choice == "8":
            save_tasks_to_file()
        elif choice == "9":
            load_tasks_from_file()
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()