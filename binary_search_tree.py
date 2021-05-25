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

    def search_for_node(self, data):
        find_node = Node(data)
        if self.root is None:
            return False
        current_node = self.root
        found = False
        while not found:
            if current_node.data == find_node.data:
                return True
            elif find_node.data > current_node.data and current_node.r_child is not None:
                current_node = current_node.r_child
            elif find_node.data <= current_node.data and current_node.l_child is not None:
                current_node = current_node.l_child
            else:
                return False

    def search_for_node_recursive(self, root, data):
        find_node = Node(data)
        if root is None:
            return False
        if root.data == find_node.data:
            return True
        elif find_node.data < root.data and root.l_child is not None:
            root = root.l_child
            result = self.search_for_node_recursive(root, data)
        elif find_node.data > root.data and root.r_child is not None:
            root = root.r_child
            result = self.search_for_node_recursive(root, data)
        else:
            return False
        return result

    def in_order_traversal(self, root):
        if root is None:
            return
        if root.l_child is not None:
            self.in_order_traversal(root.l_child)
        print(root.data)
        if root.r_child is not None:
            self.in_order_traversal(root.r_child)

    def pre_order_traversal(self, root):
        if root is None:
            return
        print(root.data)
        if root.l_child is not None:
            self.pre_order_traversal(root.l_child)
        if root.r_child is not None:
            self.pre_order_traversal(root.r_child)






