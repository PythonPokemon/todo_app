class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Aufgabe hinzugefügt:", task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Aufgabe entfernt:", task)
        else:
            print("Aufgabe nicht gefunden:", task)

    def show_tasks(self):
        if self.tasks:
            print("Aktuelle Aufgaben:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Keine Aufgaben vorhanden.")

    def run(self):
        while True:
            print("\n--- To-Do App ---")
            print("1. Aufgabe hinzufügen")
            print("2. Aufgabe entfernen")
            print("3. Aufgaben anzeigen")
            print("4. Beenden")
            choice = input("Bitte wählen Sie eine Option: ")

            if choice == "1":
                task = input("Geben Sie die Aufgabe ein: ")
                self.add_task(task)
            elif choice == "2":
                self.show_tasks()
                task_index = int(input("Geben Sie den Index der zu entfernenden Aufgabe ein: ")) - 1
                if 0 <= task_index < len(self.tasks):
                    self.remove_task(self.tasks[task_index])
                else:
                    print("Ungültiger Index.")
            elif choice == "3":
                self.show_tasks()
            elif choice == "4":
                print("Auf Wiedersehen!")
                break
            else:
                print("Ungültige Option. Bitte wählen Sie erneut.")

if __name__ == "__main__":
    app = ToDoApp()
    app.run()
