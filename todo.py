
# Fordi Python ikke har nogen interfaces, har vi lavet to skelet-klasser
class TodoList:
    items = ...

    def __init__(self):
        pass

    def add(self, title):
        pass

    def remove(self, index):
        pass

    def get(self, index):
        pass

    def list(self):
        pass

    def size(self):
        pass


class TodoCLI:
    def __init__(self):
        pass

    def start(self):
        pass

    def prompt(self, query):
        pass

    def show(self):
        pass

# Start programmet i terminalen
if __name__ == "__main__":
    TodoCLI().start()
