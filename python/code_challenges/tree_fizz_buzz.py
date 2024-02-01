from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node

def fizz_buzz_tree(tree):
    

    def clone(tree_to_clone):

        def walk(source_node):
            if source_node is None:
                return

            clone_node = value_change(Node(source_node.value))

            for source_child in source_node.children:
                cloned_child = walk(source_child)
                if cloned_child:
                    clone_node.children.append(cloned_child)

            return clone_node

        cloned_tree = KaryTree()
        cloned_tree.root = walk(tree_to_clone.root)

        return cloned_tree
    
    def value_change(node):

        new_node = node

        if  new_node.value % 5 == 0 and  new_node.value % 3 == 0:
             new_node.value = "FizzBuzz"
        elif  new_node.value % 5 == 0:
             new_node.value = "Buzz"
        elif  new_node.value % 3 == 0:
             new_node.value = "Fizz"
        else:
            new_node.value = str(new_node.value)
        
        return new_node
        
    
    return clone(tree)









