class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, val: int) -> bool:
        node = Node(val)
        if self.tail:
            self.tail.next = node
            self.tail = node
            self.size += 1
            print("Insert in the end")
            return True
        else:
            if self.head is None:
                self.head = node
                self.tail = node
                self.size += 1
                print("Inserted at Head")
                return True

    def pretty_print(self):
        if self.head:
            cur = self.head
            while cur:
                print(cur.val, end=" ")
                cur = cur.next
            print()
        else:
            print("No elements in the queue")

    def dequeu(self) -> int:
        if self.head is None:
            print("NO elements in the queue")
            return -1
        if self.head:
            res = self.head.val
            self.head = self.head.next
            return res


def test():
    q = Queue()
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    q.pretty_print()
    q.dequeu()
    q.pretty_print()


if __name__ == "__main__":
    test()
