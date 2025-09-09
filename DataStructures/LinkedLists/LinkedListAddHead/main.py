# Implement the add_to_head method. It should add a new node to the front of the list and return nothing.

# Set the "next" field of the given node to the current head node.
# Update the head reference to the given node.
from node import Node


class LinkedList:
    def add_to_head(self, node):
        if self.head is None:
            self.head = node
            return
        
        node.next = self.head
        self.head = node
        

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            return
        last_node = None
        for current_node in self:
            last_node = current_node
        last_node.set_next(node)

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
