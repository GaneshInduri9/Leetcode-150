from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorder the list in-place such that:
        L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head or not head.next:
            return

        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Step 3: Merge the two halves
        first, second = head, prev
        while second.next:
            # last node next should be pointed to the second node
            # so put second.next = first.next 
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

# Helper function to print the linked list
def printLinkedList(head: Optional[ListNode]) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Helper function to create a linked list from a list
def list_to_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Test function
def testReorderList():
    # Create a linked list
    head = list_to_linked_list([1, 2, 3, 4, 5])
    
    print("Original Linked List:")
    printLinkedList(head)

    solution = Solution()
    solution.reorderList(head)

    print("Reordered Linked List:")
    printLinkedList(head)

# Main method
if __name__ == "__main__":
    testReorderList()
