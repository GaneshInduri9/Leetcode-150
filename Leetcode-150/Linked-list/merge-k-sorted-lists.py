"""
    You are given an array of k linked lists lists, where each list is sorted in ascending order.
    Return the sorted linked list that is the result of merging all of the individual linked lists.
    ex : Input: lists = [[1,2,4],[1,3,5],[3,6]]
    Output: [1,1,2,3,3,4,5,6]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from heapq import heappush, heappop
from typing import Optional
from typing import List
class Solution: 
    """
        The most brute force way to solve this would be to convert each nodes to Array and 
        then sort and then covert them back to nodes.
        A better approach would be two merge the fisrt and second LL and then merge the result 
        this with the third ll and we can do it until the end.


        The optimal approach would be to use min heap this gives the in consant time
        we offer the first nodes of k elements and the nodes it self and then in other 
        loop until we have elements we are gonna pop elements and push the next of that poped element to heap 
    """   
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        n = len(lists)
        for i in range(n):
            if lists[i]:
                heappush(min_heap,(lists[i].val,  i,lists[i]))
        
        dummy = ListNode(-1)
        temp = dummy

        while min_heap:
            value,index, node = heappop(min_heap)
            if node.next :
                heappush(min_heap,(node.next.val,index,node.next))
            temp.next = node
            temp=temp.next
        return dummy.next
