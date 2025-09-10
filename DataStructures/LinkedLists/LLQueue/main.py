# LockedIn's queue was working just fine on small datasets, but appending items once the list has 100,000+ items has started to take a toll on our servers.
# Implement these changes to speed up our Linked List's inserts to O(1):

# add_to_head should set the tail reference to the given node if the list is empty.

# add_to_tail should:
# Set the head and tail to the given node if the list is empty
# Instead of iterating to find the last node, use the tail reference to append the new node
# Update the tail reference to new node

# The constructor should set self.tail to None. ***

from node import Node


class LinkedList:
    def add_to_head(self, node):
        if not self.head:
            self.tail = node
            
        node.set_next(self.head)
        self.head = node
        
    

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node
        # last_node = None
        # for current_node in self:
        #     last_node = current_node
        # last_node.set_next(node)

    def __init__(self):
        self.head = None
        self.tail = None

    # don't touch below this line

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
