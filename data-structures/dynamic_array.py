'''
DYNAMIC ARRAY CLASS (Similar to Python List)
'''


class DynamicArray:
    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.memory = self.make_array(self.capacity)

    def __len__(self):

        return self.length

    def __getitem__(self, index):
        if not 0 <= index < self.length:
            return IndexError('Index is out of bounds!')

        return self.memory[index]

    def append(self, ele):
        if self.length == self.capacity:
            self._resize(2 * self.capacity)

        self.memory[self.length] = ele
        self.length += 1

    def pop(self):
        return None

    def unshift(self):
        return None

    def shift(self):
        return None

    def _resize(self, new_cap):
        _memory = self.make_array(new_cap)

        for k in range(self.length):
            _memory[k] = self.memory[k]

        self.memory = _memory
        self.capacity = new_cap

    def make_array(self, new_cap):
        return [None] * new_cap