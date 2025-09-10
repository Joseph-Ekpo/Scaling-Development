# Complete the remove_from_head method. It should remove the first node from the list (the head) and return it.

# If the list is empty, just return None.
# The head should now point to the next node in the list (if there is one).
# The tail should be None if the list is now empty
# The old head's Node should no longer point to anything
from node import Node


class LLQueue:
    def remove_from_head(self):
        # If list is empty
        if not self.head:
            return None
        else:
            # If list is not empty -->
            
            new_head = self.head.next
            original_head = self.head
            self.head = new_head
            original_head.next = None
            # If there is no head, there is no tail ;)
            if not self.head:
                self.tail = None
            return original_head

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.tail = None
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
        return " <- ".join(nodes)
