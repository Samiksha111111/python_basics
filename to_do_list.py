import os

todo_list_file = "todoList.txt"

class ToDoList:
    def __init__(self, file_name=todo_list_file):
        self.file_name = file_name
        self.tasks = []
        self.load_tasks_from_file()

    def save_tasks_to_file(self):
        """Save the current tasks list to the file."""
        with open(self.file_name, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
        print("Tasks saved to file.")

    def load_tasks_from_file(self):
        """Load tasks from the file into the task list."""
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            print(f"Tasks loaded from {self.file_name}.")
        else:
            print("No saved tasks found, starting with an empty list.")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the list")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the list")
        else:
            print(f"Task '{task}' not found in the list")

    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            print(f"Task updated to '{new_task}'")
        else:
            print(f"Task '{old_task}' not found in the list")

    def show_tasks(self):
        if self.tasks:
            print("Your to do list:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
        else:
            print("Your ToDo list is empty.")


todo_list = ToDoList()


todo_list.add_task("Study for an exam")
todo_list.add_task("Finish the report")
todo_list.add_task("Talk to my parents")

todo_list.show_tasks()


todo_list.remove_task("Finish the report")
todo_list.update_task("Study for an exam", "Go for a walk")

todo_list.show_tasks()

todo_list.save_tasks_to_file()
