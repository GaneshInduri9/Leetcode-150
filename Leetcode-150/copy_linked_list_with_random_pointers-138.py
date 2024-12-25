"""
    A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
    Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
    For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
    Return the head of the copied linked list.
    The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
    Your code will only be given the head of the original linked
"""
from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
        can't we just iterate from head of the original list and make a copy
        of the original nodes and set the next reference to the new node
        the problem with this is we dont know what's the random pointers 
        pointing to well we may know for the original list we will not know 
        where this copy node random should point to solve this what we can 
        do is create a copy and store the original node to the copy node
        so when we want to set the random and next pointers we can just look at the original
        node next and random pointer values in the map this will give us the 
        new node values corrseponeded with the original nodes.


        In real interview coming up with this approach would be pretty awesome :)
    """
    def copyRandomListBruteForce(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_map = {}
        curr = head

        while curr:
            copy_map[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            # get the currents copy and set the next and random pointers to 
            # currnt node value's
            copy_node = copy_map.get(curr)
            copy_node.next = copy_map.get(curr.next)
            copy_node.random = copy_map.get(curr.random)
            curr = curr.next
        return copy_map.get(head)
    
    """
        Think about the previous brute force approach what is causing us the extra memory
        the idea to mentain the map of orinal node to copy node right, instead of map
        place the copy node in between the original node and the original node next 
        reference with this the issue is solved we can than set the random pointer for the 
        original node and then reset the original node it original state. 

        sounds pretty DAMN COOL!
    """
    def copyLLwithRandomNode(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # Place the nodes in middle
        curr = head
        while curr:
            tmp = curr.next
            curr.next = Node(curr.val)
            curr.next.next = tmp
            curr = tmp
        
        # Go ahead and set the refrences of random nodes for the copynodes 
        curr = head
        while curr:
            copy_node = curr.next
            if curr.random:
                copy_node.random = curr.random.next
            else:
                copy_node.random = None
            curr = curr.next.next
        
        # Revert the original nodes
        dummy = Node(-1)
        dummyIt = dummy
        curr = head
        while curr:
            copy_node = curr.next
            dummyIt.next = copy_node
            curr.next = copy_node.next
            curr = curr.next
            dummyIt = dummyIt.next

        return dummy.next

def print_linked_list(head):
    """ Helper function to print the linked list and its random pointers."""
    result = []
    while head:
        random_val = head.random.val if head.random else None
        result.append(f"[val: {head.val}, random: {random_val}]")
        head = head.next
    return " -> ".join(result)

def main():
    # Create the nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    # Set up the next pointers
    node1.next = node2
    node2.next = node3

    # Set up the random pointers
    node1.random = node3  # 1 -> 3
    node2.random = node1  # 2 -> 1
    node3.random = node2  # 3 -> 2

    print("Original linked list:")
    print(print_linked_list(node1))

    # Make a deep copy using Solution class
    solution = Solution()
    copied_head = solution.copyLLwithRandomNode(node1)

    print("\nCopied linked list:")
    print(print_linked_list(copied_head))

if __name__ == "__main__":
    main()