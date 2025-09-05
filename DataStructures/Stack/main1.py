# Complete the peek method. 
# It should return the top item from the stack without modifying the stack. If the stack is empty, return None.

# Complete the pop method. 
# It should remove and return the top item from the stack. If the stack is empty, return None.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        peek_item = None
        if len(self.items) > 0:
            peek_item = self.items[-1]
        return peek_item

    def pop(self):
        pop_item = None
        if len(self.items) > 0:
            pop_item = self.items[-1]
            del self.items[len(self.items) - 1]
        return pop_item
