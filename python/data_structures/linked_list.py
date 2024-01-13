class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
       

class LinkedList:

    def __init__(self):
        self.head = None
        pass

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def __str__(self):
        result = []
        cur = self.head
        string_rep = ""
        while cur:
            string_rep += f"{{ {cur.value} }} -> "
            cur = cur.next
        
        string_rep += "NULL"
        return string_rep
    
    def includes(self, value):
        
        cur = self.head
        
        while cur != None:
            if value == cur.value:
                return True
            cur = cur.next
            
        return False



class TargetError:
    pass
