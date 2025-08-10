from datetime import datetime

tasks = []

def show_tasks():
    if not tasks:
        print("\n✅ No tasks yet.")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task['completed'] else "❌"
            print(f"{i}. {task['title']} [{status}] | Deadline: {task['deadline']} | Priority: {task['priority']}")

def add_task():
    title = input("Enter task title: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    priority = input("Enter priority (High / Medium / Low): ").capitalize()

    # Validate date format
    try:
        datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("⚠️ Invalid date format. Setting deadline as 'N/A'.")
        deadline = "N/A"

    if priority not in ["High", "Medium", "Low"]:
        print("⚠️ Invalid priority. Setting as 'Low'.")
        priority = "Low"

    tasks.append({
        "title": title,
        "deadline": deadline,
        "priority": priority,
        "completed": False
    })
    print("Task added successfully! ✅")

def update_task():
    show_tasks()
    task_num = int(input("Enter task number to update: ")) - 1
    if 0 <= task_num < len(tasks):
        new_title = input("Enter new task title: ")
        new_deadline = input("Enter new deadline (YYYY-MM-DD): ")
        new_priority = input("Enter new priority (High / Medium / Low): ").capitalize()

        try:
            datetime.strptime(new_deadline, "%Y-%m-%d")
        except ValueError:
            print("⚠️ Invalid date format. Keeping old deadline.")
            new_deadline = tasks[task_num]['deadline']

        if new_priority not in ["High", "Medium", "Low"]:
            print("⚠️ Invalid priority. Keeping old priority.")
            new_priority = tasks[task_num]['priority']

        tasks[task_num]['title'] = new_title
        tasks[task_num]['deadline'] = new_deadline
        tasks[task_num]['priority'] = new_priority

        print("Task updated successfully! ✏️")
    else:
        print("Invalid task number.")

def mark_complete():
    show_tasks()
    task_num = int(input("Enter task number to mark complete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['completed'] = True
        print("Task marked as complete! ✅")
    else:
        print("Invalid task number.")

def delete_task():
    show_tasks()
    task_num = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        removed = tasks.pop(task_num)
        print(f"Task '{removed['title']}' deleted! 🗑️")
    else:
        print("Invalid task number.")

def menu():
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Mark Task Complete")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            mark_complete()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice, please try again.")

# Run the menu
menu()
