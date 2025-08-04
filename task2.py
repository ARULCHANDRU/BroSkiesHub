# todo.py

# Define the name of the file where tasks will be stored
TASKS_FILE = "tasks.txt"

def load_tasks():
    """
    Loads tasks from the tasks.txt file.
    If the file doesn't exist, it returns an empty list.
    """
    try:
        with open(TASKS_FILE, 'r') as file:
            # Read all lines from the file and use strip() to remove any trailing newline characters
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # If the file is not found, it's the first time running, so return an empty list
        tasks = []
    return tasks

def save_tasks(tasks):
    """Saves the current list of tasks to the tasks.txt file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + "\n") # Add a newline character to store each task on a new line

def view_tasks(tasks):
    """Displays all the tasks to the user."""
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("Your to-do list is empty.")
    else:
        # Enumerate adds a counter to an iterable. We use it to display numbered tasks.
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    print("-----------------------\n")

def add_task(tasks):
    """Adds a new task to the list."""
    task = input("Enter the new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added successfully!")

def remove_task(tasks):
    """Removes a task from the list."""
    view_tasks(tasks) # Show the tasks first so the user can choose which one to remove
    if not tasks:
        return # If there are no tasks, do nothing

    try:
        task_num_to_remove = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num_to_remove <= len(tasks):
            # List indices are 0-based, so we subtract 1
            removed_task = tasks.pop(task_num_to_remove - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# --- Main Program Loop ---
def main():
    # Load tasks from the file right when the program starts
    tasks = load_tasks()

    while True:
        print("What would you like to do?")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# This ensures the main() function runs when the script is executed
if __name__ == "__main__":
    main()