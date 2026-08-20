class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create a linked list
    def create(self):
        n = int(input("Enter number of nodes: "))
        for i in range(n):
            data = int(input("Enter value: "))
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node
        print("Linked list created successfully.")

    # 2. Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Node inserted at beginning.")

    # 3. Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print("Node inserted at end.")

    # 4. Insert at a specific index
    def insert_index(self, data, index):
        if index < 0:
            print("Invalid index.")
            return
        if index == 0:
            self.insert_begin(data)
            return
        new_node = Node(data)
        temp = self.head
        for i in range(index - 1):
            if temp is None:
                print("Index out of range.")
                return
            temp = temp.next
        if temp is None:
            print("Index out of range.")
            return
        new_node.next = temp.next
        temp.next = new_node
        print("Node inserted at index", index)

    # 5. Delete by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty.")
            return

        # If first node contains the value
        if self.head.data == value:
            self.head = self.head.next
            print(value, "deleted.")
            return
        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next
        if temp.next is None:
            print(value, "not found.")
        else:
            temp.next = temp.next.next
            print(value, "deleted.")

    # 6. Delete first node
    def delete_first(self):
        if self.head is None:
            print("List is empty.")
            return
        deleted = self.head.data
        self.head = self.head.next
        print(deleted, "deleted from beginning.")

    # 7. Delete last node
    def delete_last(self):
        if self.head is None:
            print("List is empty.")
            return

        # Only one node
        if self.head.next is None:
            deleted = self.head.data
            self.head = None
            print(deleted, "deleted from end.")
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        deleted = temp.next.data
        temp.next = None
        print(deleted, "deleted from end.")

    # 8. Count number of nodes
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print("Number of nodes:", count)

    # 9. Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Main program
ll = SinglyLinkedList()

while True:
    print(" SINGLY LINKED LIST")
    print("1. Create a linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at specific index")
    print("5. Delete by value")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Count number of nodes")
    print("9. Display / Traverse")
    print("10. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        ll.create()
    elif choice == 2:
        data = int(input("Enter value: "))
        ll.insert_begin(data)
    elif choice == 3:
        data = int(input("Enter value: "))
        ll.insert_end(data)
    elif choice == 4:
        data = int(input("Enter value: "))
        index = int(input("Enter index: "))
        ll.insert_index(data, index)
    elif choice == 5:
        value = int(input("Enter value to delete: "))
        ll.delete_by_value(value)
    elif choice == 6:
        ll.delete_first()
    elif choice == 7:
        ll.delete_last()
    elif choice == 8:
        ll.count_nodes()
    elif choice == 9:
        ll.display()
    elif choice == 10:
        print("Program exited.")
        break
    else:
        print("Invalid choice. Please try again.")
