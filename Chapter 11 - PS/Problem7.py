class Vector:
    def __init__(self, values):
        self.values = values

    def __len__(self):
        return len(self.values)


v = Vector([1, 2, 3])

print(len(v))