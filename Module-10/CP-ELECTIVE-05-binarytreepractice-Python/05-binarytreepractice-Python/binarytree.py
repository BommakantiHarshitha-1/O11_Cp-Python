class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """
        Return True if the find_val is in the tree and False otherwise.
        """
        # Your code goes here
        return self.preorder_search(self.root,find_val)

    def print_tree(self):
        """
        Print out all tree nodes as they are visited in a pre-order traversal."""
        # Your code goes here
        self.preorder_print(self.root)

    def preorder_search(self, start, find_val):
        """
        Helper method - use this to create a recursive search solution.
        """
        # Your code goes here
        if start ==None:
            return False
        if start.value == find_val:
            return True
        return self.preorder_search(start.left,find_val) or self.preorder_search(start.right,find_val)


    def preorder_print(self, start, traversal):
        """
        Helper method - use this to create a recursive print solution.
        """
        # Your code goes here
        if start is None:
            return 
        print(start.value)
        self.preorder-print(start.left)
        self.preorder_print(start.right)