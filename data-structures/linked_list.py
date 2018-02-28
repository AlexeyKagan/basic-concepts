class LinkedList:

    head = None
    first = None
    last = None
    length = 0

    def __repr__(self):
        return "head: %s" % self.head

    def add(self, value, position):
        _node = Node(value)

        if position == 0:
            _node.next = self.head
            self.head = _node
            return

        _prev = self.find(position - 1)

        _current = _prev.next

        _node.next = _current
        _prev.next = _node

        self.length += 1

    def find(self, position):
        found = False
        index = 0
        _node = self.head

        while not found:
            if index == position:
                found = True
            else:
                _node = _node.next
                index += 1

        return _node

    def remove(self, position):
        _prev_node = self.find(position - 1)
        _prev_node.next = _prev_node.next.next

        self.length -= 1


class Node:
    value = None
    next = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "| value: %s, next: %s" % (self.value, self.next)


linked_list = LinkedList()
linked_list.add(3, 0)
linked_list.add(4, 1)
linked_list.add(5, 2)
linked_list.add(6, 3)
linked_list.remove(2)
print linked_list