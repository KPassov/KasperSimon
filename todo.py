
# Fordi Python ikke har nogen interfaces, har vi lavet to skelet-klasser
class TodoList:
    items = []

    def __init__(self):
        pass

    def add(self, title):
        pass

    def remove(self, index):
        pass

    def get(self, index):
        return self.items[index]

    def list(self):
        return self.items

    def size(self):
        return len(self.items)


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

