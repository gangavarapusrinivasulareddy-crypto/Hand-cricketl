class BinaryTree:
    def __init__(self, size=100):
        self.tree = [None] * size
        self.size = size
    def insert(self, value):
        for i in range(self.size):
            if self.tree[i] is None:
                self.tree[i] = value
                print(value, "inserted")
                return
        print("Tree is full")
    def search(self, value):
        for i in range(self.size):
            if self.tree[i] == value:
                return i
        return -1
    def delete(self, value):
        index = self.search(value)
        if index == -1:
            print(value, "not found")
            return
        last = -1
        for i in range(self.size - 1, -1, -1):
            if self.tree[i] is not None:
                last = i
                break
        self.tree[index] = self.tree[last]
        self.tree[last] = None
        print(value, "deleted")
    def inorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
        self.inorder(2 * index + 1)
        print(self.tree[index], end=" ")
        self.inorder(2 * index + 2)
    def preorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
        print(self.tree[index], end=" ")
        self.preorder(2 * index + 1)
        self.preorder(2 * index + 2)
    def postorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
        self.postorder(2 * index + 1)
        self.postorder(2 * index + 2)
        print(self.tree[index], end=" ")
    def level_order(self):
        for value in self.tree:
            if value is not None:
                print(value, end=" ")
    def count_nodes(self):
        count = 0
        for value in self.tree:
            if value is not None:
                count += 1
        return count
    def height(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return 0
        left = self.height(2 * index + 1)
        right = self.height(2 * index + 2)
        return 1 + max(left, right)
    def display(self):
        print("Array:")
        for i in range(self.size):
            if self.tree[i] is not None:
                print(i, ":", self.tree[i])
tree = BinaryTree()
while True:
    print("\n--- Binary Tree Using Array ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Inorder")
    print("5. Preorder")
    print("6. Postorder")
    print("7. Level Order")
    print("8. Count Nodes")
    print("9. Height")
    print("10. Display")
    print("11. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        value = int(input("Enter value: "))
        tree.insert(value)
    elif choice == 2:
        value = int(input("Enter value: "))
        position = tree.search(value)
        if position != -1:
            print(value, "found at index", position)
        else:
            print(value, "not found")
    elif choice == 3:
        value = int(input("Enter value: "))
        tree.delete(value)
    elif choice == 4:
        print("Inorder:", end=" ")
        tree.inorder()
        print()
    elif choice == 5:
        print("Preorder:", end=" ")
        tree.preorder()
        print()
    elif choice == 6:
        print("Postorder:", end=" ")
        tree.postorder()
        print()
    elif choice == 7:
        print("Level Order:", end=" ")
        tree.level_order()
        print()
    elif choice == 8:
        print("Number of nodes:", tree.count_nodes())
    elif choice == 9:
        print("Height:", tree.height())
    elif choice == 10:
        tree.display()
    elif choice == 11:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
