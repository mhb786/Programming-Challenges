import math

class Vector:
    def __init__(self, arr):
        self.arr = arr
        self.len = len(arr)

    def __str__(self):
        return str(tuple(self.arr))

    def equals(self):
        return None

    def add(self, vec):
        arr = []
        if len(vec.arr) != self.len:
            return None
        else:
            for i in range(self.len):
                arr.append(self.arr[i]+vec.arr[i])
        return arr

    def subtract(self, vec):
        arr = []
        if len(vec) != self.len:
            return None
        else:
            for i in range(self.len):
                arr.append(self.arr[i] - vec.arr[i])
        return arr

    def dot(self, vec):
        total = 0
        if len(vec) != self.len:
            return None
        else:
            for i in range(self.len):
                total += self.arr[i] ** vec.arr[i]
        return total

    def norm(self):
        total = 0
        for i in range(self.len):
            total += self.arr[i] ** 2
        return math.sqrt(total)


a = Vector([1, 2, 3])
b = Vector([3, 4, 5])

print(str(a))
