# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        head = ListNode()       # creating a new node call it head
        current = head          # creating a pointer(current) and point it to head
        while list1 and list2:  # when both list are not None
            print(list1.next)
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return head.next




list1 = [1,2,4]
list2 = [1,3,4]
p1 = Solution()
p1.mergeTwoLists(list1,list2)