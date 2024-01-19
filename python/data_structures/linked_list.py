class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
       

class LinkedList:

    def __init__(self):
        self.head = None
        pass

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def __str__(self):
        result = []
        cur = self.head
        string_rep = ""
        while cur:
            string_rep += f"{{ {cur.data} }} -> "
            cur = cur.next
        
        string_rep += "NULL"
        return string_rep
    
    def includes(self, data):
        
        cur = self.head
        
        while cur != None:
            if data == cur.data:
                return True
            cur = cur.next
            
        return False
    
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
    
    def insert_after(self, where, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            raise TargetError("value not found")
        

        current = self.head
        while current:
            if current.data == where:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise TargetError("value not found")

    def insert_before(self, where, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            raise TargetError("value not found")
        

        if self.head.data == where:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head

        while current.next:
            if current.next.data == where:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise TargetError("value not found")
    
    def len_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
    
    def kth_from_end(self, n):

        traverse_counter = 0

        total_len = self.len_iterative()

        if n > total_len - 1 or n < 0:
            raise TargetError("value not found")
        
        traverse_num_node = total_len - n

        cur = self.head

        while cur and traverse_num_node - 1 > 0:
            cur = cur.next
            traverse_num_node -= 1
        return cur.data
    
    def zip_list()
           
        

class TargetError(Exception):
    print(Exception)
