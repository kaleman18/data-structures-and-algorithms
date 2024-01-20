from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.top = None

    def push(self, value):
        #Pushes a new value onto the top of the stack.

        #create a new node
        new_node = Node(value)

        # points the new node to  the current top
        new_node.next = self.top

        # reassign the self.top in the stack
        self.top = new_node

    def pop(self):
        # pops the top value from the stack

        # poping from an empty list
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        
        # get the return value
        pop_value = self.top.value

        # move the pointer which "removes" the node from the stack
        self.top = self.top.next

        return pop_value
    
    def is_empty(self):

        if self.top is None:
            return True
        
        else:
            return False
        
    def peek(self):
        
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")

        return self.top.value
    

