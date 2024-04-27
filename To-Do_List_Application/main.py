todos = ["First Task (1)"]

def add_task ():
    task = input("Enter task you want to add:")
    todos.append(f'{task} ({len(todos)+1})')

def view_tasks ():
    print(todos)

def mark_task_complete ():
    try:
        task = int(input("Enter the number of task you want to mark as complete(and delete):"))
        if 1 <= task <= len(todos):
            todos.pop(int(task)-1)
            print("Task deleted successfully.")
        else:
            print("Please enter a valid number of task you want to delete")
            mark_task_complete()
    except ValueError:
        print("Invalid input. Please enter a number")

while True:
    option = int(input("Choose an option: Add(1) Delete(2) View(3) Stop(4) "))

    if option == 1:
        add_task()
    elif option == 2:
        mark_task_complete()
    elif option == 3:
        view_tasks()
    else:
        break