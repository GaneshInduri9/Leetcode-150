class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, val):
        node = Node(val)
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
            return
        self.head = node
        self.tail = node

    def insert_at_end(self, val):
        node = Node(val)
        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            return
        self.tail = node
        self.head = node

    def delete_at_head(self):
        if not self.head:
            print("No Nodes in the DL")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delte_at_end(self):
        if not self.tail:
            print("No nodes to delete")
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
