# Complete the push method. 
# It should add an item to the top of the stack. The "top" of the stack is the end of the list in our implementation.

# Complete the size method. 
# It should return the number of items in the stack.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)
