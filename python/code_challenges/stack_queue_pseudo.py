from data_structures.stack import Stack



class PseudoQueue:

    def __init__(self):
        # inits the two stacks that 
        self.stack_one = Stack()
        self.stack_two = Stack()
    
    def enqueue(self, value):

        # assign to the first stack
        self.stack_one.push(value)


        
    def dequeue(self):

        # used to store the deleted value to return
        popped_value = None

        # moves everything from stack_one to stack_two
        while self.stack_one.top:

            temp = self.stack_one.pop()

            self.stack_two.push(temp)

        # deleting the top of stack_two which was first in stack one
        if self.stack_two.top:

            popped_value = self.stack_two.pop()

        # moves everything from stack_two back into stack_one
        while self.stack_two.top:
            
            temp = self.stack_two.pop()

            self.stack_one.push(temp)

        return popped_value

        

            

        



        
        