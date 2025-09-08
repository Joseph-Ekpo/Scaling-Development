# Complete the Node's constructor.
# Set its val field to the provided value.
# Set its next field to None.
# Complete the Node's set_next method. It should set the next field to the provided node.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    # don't touch below this line

    def __repr__(self):
        return self.val
