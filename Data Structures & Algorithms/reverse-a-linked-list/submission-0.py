# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #O(n) time, O(1) space.
        #Just flip next to prev
        #Return head when head.next is None
        if head is None:
            return None
        prev = None
        while head.next is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        head.next = prev
        return head