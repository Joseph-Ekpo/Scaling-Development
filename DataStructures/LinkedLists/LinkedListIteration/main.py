from node import Node

# The LinkedList class is a wrapper class that uses the Node class we already wrote.

# Complete the __init__ method. It should set the head field to None.
# No other node points to the linked list's head (first) node, so the LinkedList class itself needs to keep track of it. We'll use the term head and tail like this:

# head node -> node -> node -> node -> tail node

# The direction of flow above might feel opposite to what you're used to with a Queue, but it's really the same. Above I'm using arrows to show which nodes are pointing to which other nodes. In a future lesson when we implement a Queue using a LinkedList, we'll add elements to the tail and remove elements from the head.

# Complete the __iter__ method. It should be a generator function that yields each node in the linked list, from the head to the tail.
# Create a reference to the head node (e.g. node = self.head)
# Use a while loop to iterate over the linked list until node is None
# Yield the current node
# Set node to the next node

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
        

    # don't touch below this line

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)
