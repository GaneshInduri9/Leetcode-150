"""
    You are given the head of a singly linked list head and a positive integer k.
    You must reverse the first k nodes in the linked list, and then reverse the next k nodes, 
    and so on. If there are fewer than k nodes left, leave the nodes as they are.
    Return the modified list after reversing the nodes in each group of k.
    You are only allowed to modify the nodes' next pointers, not the values of the nodes.
"""
from typing import Optional
# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Helper method to print the linked list
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return "->".join(map(str, result))

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            # Find the kth node
            kth_node = self.getKthNode(prev_group_end, k)
            if not kth_node:  # If there are fewer than k nodes left
                break
            
            next_group_start = kth_node.next
            kth_node.next = None  # Detach the current group
            
            # Reverse the current group
            current_group_start = prev_group_end.next
            prev_group_end.next = self.reverseLinkedList(current_group_start)
            
            # Connect the reversed group to the next group
            current_group_start.next = next_group_start
            prev_group_end = current_group_start  # Update prev_group_end to the last node of the current group
        
        return dummy.next

    def getKthNode(self, curr: ListNode, k: int) -> ListNode:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
    def reverseLinkedList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

# Test cases
def create_linked_list(values):
    dummy = ListNode(-1)
    temp = dummy
    for val in values:
        temp.next = ListNode(val)
        temp = temp.next
    return dummy.next

def test_reverseKGroup():
    solution = Solution()

    # Test case 1: Basic test
    head = create_linked_list([1, 2, 3, 4, 5])
    k = 2
    print("Original:", head)
    print("Reversed (k=2):", solution.reverseKGroup(head, k))

    # Test case 2: Full reversal
    head = create_linked_list([1, 2, 3, 4, 5])
    k = 5
    print("Original:", head)
    print("Reversed (k=5):", solution.reverseKGroup(head, k))

    # Test case 3: Partial group at the end
    head = create_linked_list([1, 2, 3, 4, 5])
    k = 3
    print("Original:", head)
    print("Reversed (k=3):", solution.reverseKGroup(head, k))

    # Test case 4: k = 1 (No reversal)
    head = create_linked_list([1, 2, 3, 4, 5])
    k = 1
    print("Original:", head)
    print("Reversed (k=1):", solution.reverseKGroup(head, k))

    # Test case 5: Empty list
    head = create_linked_list([])
    k = 3
    print("Original:", head)
    print("Reversed (k=3):", solution.reverseKGroup(head, k))

test_reverseKGroup()
