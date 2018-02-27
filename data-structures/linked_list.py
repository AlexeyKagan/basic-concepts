class LinkedList:

    head = None
    first = None
    last = None

    def add(self, value):
        _node = Node(value)

        if not self.first:
            _node.next = None
            self.head = _node
            self.last = _node
            self.first = _node
            return

        self.last.next = _node

    def find(self):
        return None

    def remove(self):
        return None

class Node:
    value = None
    next = None

    def __init__(self, value):
        self.value = value

