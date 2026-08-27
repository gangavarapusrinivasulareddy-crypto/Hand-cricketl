class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_begin(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    # Insert at End
    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new
            new.prev = temp

    # Delete at Beginning
    def deleteAtBeg(self):
        if self.head is None:
            print("No Data to delete")
        else:
            temp = self.head
            self.head = temp.next

            if self.head is not None:
                self.head.prev = None

            print("Deleted Value =", temp.data)

    # Delete at End
    def deleteAtEnd(self):
        if self.head is None:
            print("No Data to delete")

        elif self.head.next is None:
            print("Deleted Value =", self.head.data)
            self.head = None

        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            print("Deleted Value =", temp.data)

            temp.prev.next = None

    # Delete a Value
    def delete(self, value):
        if self.head is None:
            print("No Data to delete")
            return

        temp = self.head

        # Delete first node
        if temp.data == value:
            self.head = temp.next

            if self.head is not None:
                self.head.prev = None

            print("Value deleted")
            return

        # Search for the value
        while temp and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value not present")
        else:
            # Connect previous node to next node
            temp.prev.next = temp.next

            # Connect next node to previous node
            if temp.next is not None:
                temp.next.prev = temp.prev

            print("Value deleted")

    # Count Nodes
    def count(self):
        if self.head is None:
            print("No Linked List")
        else:
            c = 0
            temp = self.head

            while temp:
                c += 1
                temp = temp.next

            print("Number of nodes =", c)

    # Display from Beginning to End
    def display(self):
        if self.head is None:
            print("No Linked List")
        else:
            temp = self.head

            while temp:
                print(temp.data, end=" <-> ")
                temp = temp.next

            print("None")


# Create Doubly Linked List
dll = DoublyLinkedList()


# Menu
while True:
    print("\n--- Doubly Linked List ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete at Beginning")
    print("4. Delete at End")
    print("5. Delete a Value")
    print("6. Count Nodes")
    print("7. Display")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        dll.insert_begin(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        dll.insert_end(data)

    elif choice == 3:
        dll.deleteAtBeg()

    elif choice == 4:
        dll.deleteAtEnd()

    elif choice == 5:
        value = int(input("Enter value to delete: "))
        dll.delete(value)

    elif choice == 6:
        dll.count()

    elif choice == 7:
        dll.display()

    elif choice == 8:
        print("Program ended")
        break

    else:
        print("Invalid choice")
