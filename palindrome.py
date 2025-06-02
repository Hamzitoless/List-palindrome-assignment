class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #Initializes the next and previous pointers to none
        self.prev = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node =Node(data)
        if self.top: #If stack is not empty, link new node to current top
            new_node.next = self.top
            self.top.prev = new_node
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        data=self.top.data
        self.top = self.top.next
        if self.top:
            self.top.prev = None
        return data

    def is_empty(self):
        return self.top is None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail =new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return data

    def is_empty(self):
        return self.head is None

def is_palindrome_using_stack(s: str):
    if not s:
        return True

    stack = Stack()
    queue = Queue()

    for char in s:
        stack.push(char)
        queue.enqueue(char)

    while not stack.is_empty() and not queue.is_empty():
        if stack.pop() !=queue.dequeue():
            return False

    return True




