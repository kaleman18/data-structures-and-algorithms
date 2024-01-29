from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def add(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            return 

        def walk(node, node_to_add):
            if node_to_add.value < node.value:
                if node.left is None:
                    node.left = node_to_add
                else:
                    walk(node.left, node_to_add)
            else: # node_to_add.value >= value
                if node.right is None:
                    node.right = node_to_add
                else:
                    walk(node.right, node_to_add)
        walk(self.root, node)

    def contains(self, value):

        search_value = value

        def walk(node, value_seacrh):

            if node is None:
                return False
            
            if value_seacrh == node.value:
                return True
            elif value_seacrh < node.value:
                walk(node.left, value_seacrh)
            else:
                walk(node.right, value_seacrh)

        

            
