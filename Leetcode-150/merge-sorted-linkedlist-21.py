from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Brute Force:
    - Time Complexity: O(n log n), where n is the total number of nodes across both lists due to sorting.
    - Space Complexity: O(n), as we store all nodes in a list for sorting.

    Optimal Solution:
    - Time Complexity: O(n + m), where n and m are the lengths of the two linked lists.
    - Space Complexity: O(1), as no extra data structures are used.
    """

    def mergeTwoListsBruteForce(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:  # Handle both lists being empty
            return None

        # Step 1: Collect all nodes in a list
        nodes = []
        while list1:
            nodes.append(list1)
            list1 = list1.next
        while list2:
            nodes.append(list2)
            list2 = list2.next
        
        # Step 2: Sort the nodes based on their values
        nodes.sort(key=lambda node: node.val)
        
        # Step 3: Reconstruct the linked list
        dummy = ListNode(0)
        current = dummy
        for node in nodes:
            current.next = node
            current = current.next
        
        # Step 4: Ensure the last node points to None
        current.next = None
        return dummy.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Optimal Solution:
        Merge two sorted lists by directly comparing node values.
        """
        dummy = ListNode(0)
        current = dummy

        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining nodes from either list
        current.next = list1 if list1 else list2

        return dummy.next

# Helper function to print the linked list
def printLinkedList(head: Optional[ListNode]):
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

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values

# Test function
def testMergeTwoLists():
    # Create two linked lists
    list1 = list_to_linked_list([1, 2, 4])
    list2 = list_to_linked_list([1, 3, 4])

    solution = Solution()

    print("Testing Brute Force Merge:")
    print("List1:")
    printLinkedList(list1)
    print("List2:")
    printLinkedList(list2)

    # Test brute force merge
    mergedBruteForce = solution.mergeTwoListsBruteForce(list1, list2)
    print("Merged List (Brute Force):")
    printLinkedList(mergedBruteForce)

    # Recreate the lists for the next test (as they are mutated during merging)
    list1 = list_to_linked_list([1, 2, 4])
    list2 = list_to_linked_list([1, 3, 4])

    print("\nTesting Optimal Merge:")
    print("List1:")
    printLinkedList(list1)
    print("List2:")
    printLinkedList(list2)

    # Test optimal merge
    mergedOptimal = solution.mergeTwoLists(list1, list2)
    print("Merged List (Optimal):")
    printLinkedList(mergedOptimal)

# Main method
if __name__ == "__main__":
    testMergeTwoLists()
