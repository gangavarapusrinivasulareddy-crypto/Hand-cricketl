class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


top = None


def push():
    global top

    element = int(input("Enter element to push: "))

    new_node = Node(element)
    new_node.next = top
    top = new_node

    print(element, "pushed into stack")


def pop():
    global top

    if top is None:
        print("Stack is empty")
    else:
        print(top.data, "popped from stack")
        top = top.next


def peek():
    if top is None:
        print("Stack is empty")
    else:
        print("Top element is:", top.data)


def display():
    if top is None:
        print("Stack is empty")
    else:
        temp = top
        print("Stack elements are:")

        while temp is not None:
            print(temp.data)
            temp = temp.next


while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()

    elif choice == 2:
        pop()

    elif choice == 3:
        peek()

    elif choice == 4:
        display()

    elif choice == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")
