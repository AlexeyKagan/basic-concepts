class List:
    memory = []
    length = 0

    def __init__(self, items):
        self.memory = items
        self.length = len(items)

    def push(self, *items):
        self.memory += items
        self.length += len(items)

        return self.length

    def pop(self):
        length = self.length - 1
        item = self.memory[length]
        _item = item
        self.length -= 1

        del self.memory[length]

        return _item

    def shift(self):
        item = self.memory[0]
        self.memory = self.memory[1:]
        self.length -= 1

        return item

    def unshift(self, item):
        self.memory = [item] + self.memory[0:]
        self.length += 1

        return self.length


list = List([1, 2, 3])
list.push(6, 2)
list.pop()
list.shift()
list.unshift(99)

print list.memory
print list.length
