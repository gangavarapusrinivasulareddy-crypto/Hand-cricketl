class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
front = None
rear = None
def enqueue():
    global front, rear
    value = int(input("Enter the value to enqueue: "))
    new_node = Node(value)
    if front is None:
        front = new_node
        rear = new_node
        rear.next = front
    else:
        new_node.next = front
        rear.next = new_node
        rear = new_node
    print(value, "inserted into the queue.")
def dequeue():
    global front, rear
    if front is None:
        print("Queue Underflow! Queue is empty.")
        return
    value = front.data
    if front == rear:
        front = None
        rear = None
    else:
        front = front.next
        rear.next = front
    print(value, "deleted from the queue.")
def peek():
    if front is None:
        print("Queue is empty!")
    else:
        print("Front element:", front.data)
def display():
    if front is None:
        print("Queue is empty!")
        return
    print("Queue elements:")
    temp = front
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == front:
            break
    print()
while True:
    print("\n--- CIRCULAR QUEUE USING LINKED LIST ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program terminated.")
        break
    else:
        print("Invalid choice! Please try again.")
