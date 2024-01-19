class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def zip_lists(a, b):

    node = Node()

    cur = node

    while a or b:
        if a:
            cur.next = a
            a = a.next
            cur = cur.next

        if b:
            cur.next = b
            b = b.next
            cur = cur.next
    return node
