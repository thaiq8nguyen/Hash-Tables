class DynamicArray:
    def __init__(self, capacity=0):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        if index >= self.count:
            return ("Index out of bound!")
