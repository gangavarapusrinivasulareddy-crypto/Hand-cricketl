MAX = 5
queue = [None] * MAX
front = -1
rear = -1
def enqueue():
    global front, rear
    if rear == MAX - 1:
        print("Queue Overflow!")
        return
    value = int(input("Enter the value to enqueue: "))
    if front == -1:
        front = 0
    rear += 1
    queue[rear] = value
    print(value, "inserted into the queue.")
def dequeue():
    global front, rear
    if front == -1 or front > rear:
        print("Queue Underflow!")
        return
    value = queue[front]
    print(value, "deleted from the queue.")
    front += 1
    if front > rear:
        front = -1
        rear = -1
def peek():
    if front == -1 or front > rear:
        print("Queue is empty!")
    else:
        print("Front element:", queue[front])
def display():
    if front == -1 or front > rear:
        print("Queue is empty!")
        return
    print("Queue elements:")
    for i in range(front, rear + 1):
        print(queue[i], end=" ")
    print()
while True:
    print("\n--- QUEUE USING ARRAY ---")
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
        print("Invalid choice!")
