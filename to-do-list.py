todo_list = []

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print("✅ Task added!")

def view_tasks():
    if not todo_list:
        print("📌 No tasks found!")
    else:
        print("\n📋 To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("\nEnter task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"🗑️ Removed: {removed}")
            else:
                print("❌ Invalid task number!")
        except ValueError:
            print("❌ Please enter a valid number.")

def main():
    while True:
        print("\n📌 Simple To-Do List 📌")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
