#Advanced stack implementation using linked list (Conceptual for large data)
#Sometimes, stacks are implemented using linked lists
#To avoid resizing issues with lists and to practice pointer manipulation

#Node class for linked lists
class StackNode:
    def __init__(self, value):
        self.value = value #Store the node's data
        self.next = None #Pointer to the next node (below in stack)

#Stack implemented using linked list
class LinkedListStack:
    def __init__(self):
        self.top= None #Points to the top node in the stack

    def is_empty(self):
        #Stack is empty if the top pointer is none
        return self.top is None

    def push(self, value):
        #Create a new node with the value
        new_node = StackNode(value)

        #New node's next pointer should point to the current top node
        new_node.next = self.top

        #Update top pointer to new node(new top of the stack)
        self.top= new_node

    def pop(self):
        #If stck is empty, raise error
        if self.is_empty():
            raise Exception("Cannot pop from an empty stack!")

        #Retrieve value from the top node
        popped_value = self.top.value

        #Move top pointer to the next node down the stack
        self.top = self.top.next

        #Return popped value
        return popped_value

    def peek(self):
        #Return top element value without removing it
        if self.is_empty():
            raise Exception("Cannot peek from an empty stack!")
        return self.top.value

    def display(self):
        #Print stack from top to bottom
        current = self.top
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print("Stack from top to bottom:", "-> ".join(values))

#Example usage
if __name__ == "__main__":
    stack_11= LinkedListStack()
    stack_11.push(5)
    stack_11.push(10)
    stack_11.push(15)

    stack_11.display() #Expected stack from top to bottom: 15->10 ->5

    print("peek top:", stack_11.peek()) # Output:15

    print("Pop :", stack_11.pop()) #Output :15
    stack_11.display() #Expected: 10->5

