from node import Node

class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        leaf = self.root
        while True:
            if leaf.l_child is None and leaf.r_child is None:
                if new_node.data > leaf.data:
                    leaf.r_child = new_node
                    return
                else:
                    leaf.l_child = new_node
                    return
            elif new_node.data > leaf.data:
                if leaf.r_child is not None:
                    leaf = leaf.r_child
                else:
                    leaf.r_child = new_node
                    return
            else:
                if leaf.l_child is not None:
                    leaf = leaf.l_child
                else:
                    leaf.l_child = new_node
                    return
