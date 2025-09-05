# Implement the following operations on the Queue class:

# queue.push(item): Adds an item to the tail of the queue (index 0 of list)
# queue.pop(): Removes and returns an item from the head of the queue (last index of list)
# queue.peek(): Returns an item from the head of the queue
# queue.size(): Returns the number of items in the queue

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        popped_item = None
        if len(self.items) > 0:
            popped_item = self.items[-1]
            del self.items[-1]
        return popped_item

    def peek(self):
        return None if not self.items else self.items[-1]

    def size(self):
        return len(self.items)

