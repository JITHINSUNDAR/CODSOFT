tasks = []
def add_task(tasks, task_description):
    tasks.append({'description': task_description, 'completed': False})

def view_tasks(tasks):
    for idx, task in enumerate(tasks, start=1):
        status = 'Done' if task['completed'] else 'Not Done'
        print(f"{idx}. {task['description']} - {status}")

def complete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True

def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)

import json

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Save and Exit")
        print("6. Exit without Saving")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_description = input("Enter task description: ")
            add_task(tasks, task_description)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            complete_task(tasks, task_index)
        elif choice == '4':
            task_index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, task_index)
        elif choice == '5':
            save_tasks(tasks)
            break
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

import tkinter as tk
from tkinter import messagebox

tasks = load_tasks()

def add_task():
    task_description = task_entry.get()
    if task_description:
        add_task(tasks, task_description)
        task_entry.delete(0, tk.END)
        update_task_listbox()

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task['description'])

app = tk.Tk()
app.title("To-Do List")

task_entry = tk.Entry(app, width=50)
task_entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(app, width=50, height=10)
task_listbox.pack(pady=10)

app.mainloop()
