"""
    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
    Implement the LRUCache class:
    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    The functions get and put must each run in O(1) average time complexity.
"""

"""
    Please read question properly dont be an idiot again this says least recent used one
    not most recent one was wasted an hour thinking that it was about most recent one
    anyway here is the approach: the immidiate thought when we want a key and value is
    a map but we need ro keep tarck of the least recent visted elements weather it's from 
    get or put so when ever the capacity becomes over we need to delete the least recent ones 
    so to keep track of the elements we need to an dynamic array array list or something like that 
    so when ever get or put is called we can update the ending and begging with respect to that 
    but this comes at cost it will be expensive o(n) when deleteing that requires shifting of elements.
"""

"""
    Use double linked list to solve this probelem we can insert at the beginign and delete at the end in o(1)
    now when get is called we can get the node and make it the most recent i.e make this node as next reference 
    to head pointer and for the put method we check if the insertion gonna cause the > map size greater than 
    the capacity if so we need to delte the last node which will be least recent node and then we can insert this node 
    in the bedinning and then set the reference of this node to the map key
"""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}  # HashMap to store key and corresponding node
        self.head = None  # Pointer to the most recently used node
        self.tail = None  # Pointer to the least recently used node
        self.capacity = capacity  # Capacity of the cache

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map.get(key)
            self._move_to_head(node)  # Corrected: Use a helper to move the node to the head
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map.get(key)
            node.value = value
            self._move_to_head(node)  # Corrected: Moved existing node to the head after updating
        else:
            if len(self.map) >= self.capacity:  # Corrected: Proper condition for exceeding capacity
                self._remove_tail()  # Corrected: Remove the least recently used node
            new_node = Node(key, value)
            self.map[key] = new_node
            self._add_to_head(new_node)  # Corrected: Add the new node to the head of the DLL

    def _delete_node(self, node):
        """Helper to remove a node from the DLL."""
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:  # Corrected: Update head if node is the head
            self.head = node.next
        if node == self.tail:  # Corrected: Update tail if node is the tail
            self.tail = node.prev
        node.prev = None
        node.next = None

    def _add_to_head(self, node):
        """Helper to add a node to the head of the DLL."""
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:  # Corrected: Update tail if the list was empty
            self.tail = node

    def _move_to_head(self, node):
        """Helper to move an existing node to the head of the DLL."""
        self._delete_node(node)  # Corrected: Remove node from its current position
        self._add_to_head(node)  # Add the node to the head

    def _remove_tail(self):
        """Helper to remove the tail node (least recently used)."""
        if self.tail:
            del self.map[self.tail.key]  # Corrected: Remove tail node from map
            self._delete_node(self.tail)  # Remove tail from DLL

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)