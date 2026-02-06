from task_manager import add_task, list_tasks

def main():

    choice = ""

    print("Welcome to Task Manager")

    while choice != "3":
        print("\n1. Add task")
        print("2. List tasks")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Task title: ")
            add_task(title)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            print("Gooodbye!")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
