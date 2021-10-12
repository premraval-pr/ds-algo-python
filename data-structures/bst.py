class Node:

    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


class BST:

    def __init__(self):
        self.root = None

    # insert
    def insert(self, data):
        if self.root is None:
            self.root = Node(data=data, parent=None)
        else:
            self.insert_node(data, self.root)

    # actual insertion // O(logN) if the tree is balanced else O(N)
    def insert_node(self, data, node):

        if data < node.data:
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left = Node(data, node)
        else:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = Node(data, node)

    def inorder(self):
        if self.root:
            self.inorder_traverse(self.root)

    def inorder_traverse(self, node):
        if node.left:
            self.inorder_traverse(node.left)

        print(node.data)

        if node.right:
            self.inorder_traverse(node.right)

    def get_max(self):
        if self.root:
            return self.get_max_value(self.root)

    def get_max_value(self, node):
        if node.right:
            return self.get_max_value(node.right)
        return node.data

    def get_min(self):
        if self.root:
            return self.get_min_value(self.root)

    def get_min_value(self, node):
        if node.left:
            return self.get_min_value(node.left)
        return node.data

    # remove
    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    # actual removing
    def remove_node(self, data, node):

        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left)
        elif data > node.data:
            self.remove_node(data, node.right)
        else:
            if node.left is None and node.right is None:
                print("Removing a leaf node..." + str(node.data))

                parent = node.parent

                if parent is not None and parent.left == node:
                    parent.left = None
                if parent is not None and parent.right == node:
                    parent.right = None

                if parent is None:
                    self.root = None

                del node
            elif node.left is None and node.right is not None:
                print("Removing a node with single right child")

                parent = node.parent

                if parent is not None:
                    if parent.left == node:
                        parent.left = node.right
                    if parent.right == node:
                        parent.right = node.right
                else:
                    self.root = node.right

                node.right.parent = parent
                del node
            elif node.left and not node.right:
                print("Removing a node with single left child")

                parent = node.parent

                if parent is not None:
                    if parent.left == node:
                        parent.left = node.left
                    if parent.right == node:
                        parent.right = node.left
                else:
                    self.root = node.left

                node.left.parent = parent
                del node
            else:
                print("Removing a node with 2 children")

                predecessor = self.get_predecessor(node.left)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    # getting the predecessor
    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)
        return node


bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(3)
bst.insert(1)
bst.insert(6)
bst.insert(5)
bst.insert(7)
bst.remove(3)
print("INORDER-----")
bst.inorder()
