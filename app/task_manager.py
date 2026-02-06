tasks = []

def add_task(title):
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)

def list_tasks():
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "TODO"
        print(f"{i+1}. [{status}] {task['title']}")