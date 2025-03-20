from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Brute Force:
    - Time Complexity: O(n), where n is the number of nodes in the linked list. Traversing the list and reversing takes linear time.
    - Space Complexity: O(n) due to the additional list used to store node references.

    Optimal Solution:
    - Time Complexity: O(n), as we iterate through the linked list once.
    - Space Complexity: O(1), as no extra data structures are used; reversal is done in-place.
    """

    def reverseListBruteForce(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:  # Handle empty list
            return None

        # Step 1: Collect all nodes in a list
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next

        # Step 2: Reverse the links using the collected nodes
        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].next = nodes[i - 1]

        # Step 3: Set the next reference of the new tail to None
        nodes[0].next = None

        # Step 4: Return the new head
        return nodes[-1]

    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Optimal Solution:
        The idea is to reverse the `next` pointer for each node in a single pass through the list,
        using three pointers: `prev`, `curr`, and `next`.

        Steps:
        1. Initialize `prev` to None and `curr` to the head of the list.
        2. Iterate through the list while `curr` is not None:
           - Store the next node (`next = curr.next`).
           - Reverse the current node's pointer (`curr.next = prev`).
           - Move `prev` and `curr` forward (`prev = curr`, `curr = next`).
        3. After the loop, `prev` will be the new head of the reversed list.
        """
        if not head:
            return None

        # Setup the pointers
        prev = None
        curr = head
        next = None

        while curr:
            next = curr.next  # Save the next node
            curr.next = prev  # Reverse the current node's pointer
            prev = curr  # Move prev to the current node
            curr = next  # Move curr to the next node

        return prev  # New head of the reversed list


# Helper function to print the linked list
def printLinkedList(head: Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# Test function
def testReverseLinkedList():
    # Create the linked list 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()

    print("Testing Brute Force Reversal:")
    print("Original Linked List:")
    printLinkedList(head)

    # Test brute force reversal
    reversedHeadBruteForce = solution.reverseListBruteForce(head)
    print("Reversed Linked List (Brute Force):")
    printLinkedList(reversedHeadBruteForce)

    # Restore the original list for the next test
    head = solution.reverseLinkedList(reversedHeadBruteForce)

    print("\nTesting Optimal Reversal:")
    print("Original Linked List:")
    printLinkedList(head)

    # Test optimal reversal
    reversedHeadOptimal = solution.reverseLinkedList(head)
    print("Reversed Linked List (Optimal):")
    printLinkedList(reversedHeadOptimal)


# Main method
if __name__ == "__main__":
    testReverseLinkedList()
