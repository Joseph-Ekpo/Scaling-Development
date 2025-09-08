from node import Node


class LinkedList:
    def __init__(self):
        pass

    def __iter__(self):
        pass

    # don't touch below this line

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)
