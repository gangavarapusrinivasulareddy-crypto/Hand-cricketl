MAX = 5
queue = [None] * MAX
front = -1
rear = -1
def enqueue():
    global front, rear
    if (rear + 1) % MAX == front:
        print("Queue Overflow! Circular Queue is full.")
        return
    value = int(input("Enter the value to enqueue: "))
    if front == -1:
        front = 0
        rear = 0
    else:
        rear = (rear + 1) % MAX
    queue[rear] = value
    print(value, "inserted into the queue.")
def dequeue():
    global front, rear
    if front == -1:
        print("Queue Underflow! Circular Queue is empty.")
        return
    value = queue[front]
    print(value, "deleted from the queue.")
    if front == rear:
        front = -1
        rear = -1
    else:
        front = (front + 1) % MAX
def peek():
    if front == -1:
        print("Queue is empty!")
    else:
        print("Front element:", queue[front])
def display():
    if front == -1:
        print("Queue is empty!")
        return
    print("Queue elements:")
    i = front
    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % MAX
    print()
while True:
    print("\n--- CIRCULAR QUEUE USING ARRAY ---")
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
