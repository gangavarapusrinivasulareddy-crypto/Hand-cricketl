class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]

    def insert(self, key):
        index = key % self.size
        self.table[index].append(key)

    def display(self):
        print("Separate Chaining:")
        for i in range(self.size):
            print(i, ":", self.table[i])
            
class LinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [-1] * size

    def insert(self, key):
        index = key % self.size

        while self.table[index] != -1:
            index = (index + 1) % self.size

        self.table[index] = key

    def display(self):
        print("\nLinear Probing:")
        for i in range(self.size):
            print(i, ":", self.table[i])

class QuadraticProbing:
    def __init__(self, size):
        self.size = size
        self.table = [-1] * size

    def insert(self, key):
        index = key % self.size
        i = 0

        while self.table[(index + i * i) % self.size] != -1:
            i += 1

        self.table[(index + i * i) % self.size] = key

    def display(self):
        print("\nQuadratic Probing:")
        for i in range(self.size):
            print(i, ":", self.table[i])

size = 7
keys = [10, 20, 15, 7, 22]

h1 = HashTable(size)
h2 = LinearProbing(size)
h3 = QuadraticProbing(size)

for key in keys:
    h1.insert(key)
    h2.insert(key)
    h3.insert(key)

h1.display()
h2.display()
h3.display()
