# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Can do this two ways, single pass with 2 pointers spaced n apart
        #Or two runs, one to find length of list
        #then a second to get to len - n to change the value
        top = head
        slow = head
        fast = head
        count = 0
        while count < n:
            if fast.next is not None:
                fast = fast.next
                count += 1
            else:
                #need to remove head.
                return top.next
        #Now, they're n spaces apart.
        #Iterate until N.next is none.
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return top

