from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def append_node(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.tail.next = new_node
            self.tail = self.tail.next


