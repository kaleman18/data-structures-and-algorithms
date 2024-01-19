class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        pass

    def add_begin(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_after_value(self, where, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current:
            if current.data == where:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def add_before_value(self, where, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

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

        