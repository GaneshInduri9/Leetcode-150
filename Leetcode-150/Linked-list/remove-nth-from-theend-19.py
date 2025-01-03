"""
    You are given the beginning of a linked list head, and an integer n.
    Remove the nth node from the end of the list and return the beginning of the list.
    Input: head = [1,2,3,4], n = 2
    Output: [1,2,4]
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEndBruteForce(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Collect all nodes in a list
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
        
        # Step 2: Find the node to remove (nth from end)
        length = len(nodes)
        if n == length:  # Special case: removing the head node
            return head.next
        
        # Step 3: Remove the nth node from the end
        nodes[length - n - 1].next = nodes[length - n].next
        return head

    def removeNthFromEndOptimal(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases (e.g., removing head)
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Step 1: Move `first` pointer n steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Step 2: Move both `first` and `second` until `first` reaches the end
        while first:
            first = first.next
            second = second.next
        
        # Step 3: Remove the nth node from the end
        second.next = second.next.next
        
        return dummy.next  # Return the new head

# Helper function to print the linked list
def printLinkedList(head: Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Test function
def testRemoveNthFromEnd():
    # Create the linked list 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()

    print("Testing Brute Force Approach:")
    print("Original Linked List:")
    printLinkedList(head)

    # Test brute force removal
    newHeadBruteForce = solution.removeNthFromEndBruteForce(head, 2)
    print("Linked List After Removing 2nd Node from the End (Brute Force):")
    printLinkedList(newHeadBruteForce)

    # Restore the original list for the next test
    head = solution.removeNthFromEndOptimal(newHeadBruteForce, 2)

    print("\nTesting Optimal Approach:")
    print("Original Linked List:")
    printLinkedList(head)

    # Test optimal removal
    newHeadOptimal = solution.removeNthFromEndOptimal(head, 2)
    print("Linked List After Removing 2nd Node from the End (Optimal):")
    printLinkedList(newHeadOptimal)

# Main method
if __name__ == "__main__":
    testRemoveNthFromEnd()

        