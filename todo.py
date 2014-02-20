
# Fordi Python ikke har nogen interfaces, har vi lavet to skelet-klasser
class TodoList:
    """Class for a TodoList"""
    items = []

    def __init__(self):
        """TodoList constructor"""
        pass

    def add(self, title):
        """adds the element title to the TodoList returning the new list"""
        return self.items.append(title)

    def remove(self, index):
        """removes the element at index from the TodoList returning the new
        list"""
        return self.items.pop(index)

    def get(self, index):
        """Returns the value at index"""
        return self.items[index]

    def list(self):
        """Returns the mutable TodoList"""
        return self.items

    def size(self):
        """Returns the size of the TodoList"""
        return len(self.items)


class TodoCLI:
    def __init__(self):
        """Constructor for the prompt client for a TodoList"""
        pass

    def start(self):
        """Starts an interaction with the user"""
        pass

    def prompt(self, query):
        """Prompts the user for some input"""
        pass

    def show(self):
        pass

# Start programmet i terminalen
if __name__ == "__main__":
    TodoCLI().start()

