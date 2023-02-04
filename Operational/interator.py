class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.data):
            val = self.data[self.idx]
            self.idx += 1
            return val
        else:
            raise StopIteration


data = CustomIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for item in data:
    print(item)


data2 = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
next(data2)
next(data2)
value = next(data2)
print(value)