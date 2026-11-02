# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Just keep a hash map of nexts. If seen before, return 1?
        #This requires O(n) space though.
        #Fast and slow pointers? This is the trick
        if head is None:
            return False
        if head.next is None:
            return False
        slow = head
        fast = head.next
        while fast is not None:
            if fast == slow:
                return True
            slow = slow.next
            if fast.next is None:
                return False
            fast = fast.next.next
        return False