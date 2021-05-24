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

    def add_to_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def contains_node(self, data):
        if self.head is None:
            return False
        find_node = Node(data)
        current_node = self.head
        found = False
        while not found:
            if current_node.data == find_node.data:
                return True
            elif current_node.next is None:
                return False
            else:
                current_node = current_node.next
