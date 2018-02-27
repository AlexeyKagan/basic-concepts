class LinkedList:

    head = None
    first = None
    last = None
    length = 0

    def add(self, value, position):
        _node = Node(value)

        if not self.first:
            _node.next = None
            self.head = _node
            self.last = _node
            self.first = _node
            return

        _prev = self.find(position - 1)
        _current = _prev.next

        _node.next = _current
        _prev.next = _node

        self.length += 1

    def find(self, position):
        return None

    def remove(self):
        return None

class Node:
    value = None
    next = None

    def __init__(self, value):
        self.value = value

