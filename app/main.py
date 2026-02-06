from task_manager import add_task

def main():

    choice = ""

    print("Welcome to Task Manager")

    while choice != "2":
        print("\n1. Add task")
        print("2. Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Task title: ")
            add_task(title)

        elif choice == "2":
            print("Goodbye!")

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
