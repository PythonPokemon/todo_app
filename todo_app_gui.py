import tkinter as tk
from tkinter import messagebox

class ToDoAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")

        self.tasks = []

        self.task_entry = tk.Entry(self.root)
        self.task_entry.pack(padx=10, pady=5)

        self.add_button = tk.Button(self.root, text="Aufgabe hinzufügen", command=self.add_task)
        self.add_button.pack(padx=10, pady=5)

        self.remove_button = tk.Button(self.root, text="Aufgabe entfernen", command=self.remove_task)
        self.remove_button.pack(padx=10, pady=5)

        self.task_listbox = tk.Listbox(self.root)
        self.task_listbox.pack(padx=10, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            self.tasks.pop(index)
            self.task_listbox.delete(index)
            messagebox.showinfo("Entfernt", f"Aufgabe '{task}' wurde entfernt.")
        else:
            messagebox.showwarning("Fehler", "Bitte eine Aufgabe auswählen.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoAppGUI(root)
    root.mainloop()
