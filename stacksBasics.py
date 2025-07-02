"""
A stack is adata structure that follows the LIFO principle-Last In First Out.
Think of a stack like a stack of plates: you put plates on top(push), and you can take plates from the top(pop),
you can only access the top plates, not the ones below.
"""
"""
----Basic stack operations----
-Push: Add an element to the top of the stack
-Pop: Remove an element from the top of the stack 
Peek/top: Look at the top of an element without removing it
Is Empty: Check if the stack has any elements
"""
#We will use the first python inbuilt method for stacks:List because it supports .append(), push() and pop() methods

stack = [10, 20, 30]  #Creates an empty list to represent the stack

print("Stack after pushes: ", stack) #Output:[10,20,30]

# To peek at the rop element(Last element in the list)
top_element=stack[-1] #Access last element without removing it
print("Top element: ", top_element) #output:30

#To check if the stack is empty
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")

#The second method, is via custom classes, Here we implant a stack class with all the key operations.
class SimpleStack:
    def __init__(self):
        #Initialize an empty list to hold stack elements
        self.items = []

    def is_empty(self):
        #Return true if the stack has no elements, otherwise return false
        return len(self.items) == 0

    #Add item to the top of the stack
    def push(self, item):
        self.items.append(item)

    #Remove an item from the top and return it
    def pop(self):
        # If stack is empty return an error to avoid an invalid operation
        if self.is_empty():
            raise Exception("Cannot pop from an empty stack")
        return self.items.pop()

    #PEEK: Return the top item without removing it
    def peek(self):
        #Raise an error if stack is empty
        if self.is_empty():
            raise Exception("Cannot peek from an empty stack")
        #The top most element is the last element to be pushed,
        #Since actual size of list is greater than position by one,
        #Minus 1 returns the last element
        return self.items[-1]

    #SIZE :Return the size of all the items in the stack
    def size(self):
        return len(self.items)

    def print_stack(self):
        #print all the items in the stack from bottom to top
        print("Stack from bottom to top: ", self.items)
        return

#Main meal
if __name__ == "__main__":
    #Instantiate the class stack by creating an object for it
    stack1 =  SimpleStack()

    #Then,push some elements
    stack1.push(100)
    stack1.push(200)
    stack1.push(300)

    #Print the elements
    stack1.print_stack()

    #Peek top element
    print("Top element: ", stack1.peek()) #Output:300

    #pop elements
    print("popped element: ", stack1.pop()) #Output :300
    stack1.print_stack() #Output :[100,200]

    #Check if empty
    print("Is stack empty? ",stack1.is_empty()) #Expected output:False

    #Pop all to empty
    stack1.pop()
    stack1.pop()
    print("Is stack empty after popping all? ", stack1.is_empty())