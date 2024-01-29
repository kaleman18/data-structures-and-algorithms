from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        # initialization here
        self.front = None
        self.back = None

    def enqueue(self, value):
        
        new_node = Node(value)

        # checks if the queue is empty
        if self.back is None:
            self.front = new_node
            self.back = new_node

        # do this if the queue isn't empty
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):

        if self.front is None:
            raise InvalidOperationError
        
        
        # get the value
        dequeue_value = self.front.value

        # move the front pointer to its next
        self.front = self.front.next

        # check if the queue has become empty
        if self.front is None:

            # update self.back
            self.back = None

        return dequeue_value
    
    def peek(self):

        if self.back is None:
            raise InvalidOperationError
        
        return self.front.value
    
    def is_empty(self):

        if self.front is None:
            return True
        
        else:
            return False
    
