class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None
        

    def pre_order(self):
        
        def walk(node):
            """Root -> Left -> Right"""
            if node is None:
                return []

            result = [node.value]
            """Recursive calls"""
            left_result = walk(node.left)
            right_result = walk(node.right)

            return result + left_result + right_result
        
        return walk(self.root)
    
    def in_order(self):
        
        def walk(node):
            """Left -> Root -> Right"""
            if node is None:
                return []

            left_result = walk(node.left)
            result = [node.value]
            right_result = walk(node.right)

            return left_result + result + right_result
        
        return walk(self.root)
    
    def post_order(self):
        
        def walk(node):
            """Left -> Right -> Root"""
            if node is None:
                return []

            left_result = walk(node.left)
            right_result = walk(node.right)
            result = [node.value]

            return left_result + right_result + result
        
        return walk(self.root)



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

