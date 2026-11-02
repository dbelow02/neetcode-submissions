# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        #Alright, regular case now.
        #Know the linked lists are sorted
        #So, keep both, increment only when < other
        #Get head:
        if list1.val < list2.val:
            prev = list1
            list1 = list1.next
        else:
            prev = list2
            list2 = list2.next
        head = prev
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                prev.next = list2
                prev = list2
                list2 = list2.next

        if list1 is None:
            #connect list1 to the rest of list2
            prev.next = list2
        elif list2 is None:
            #connect list2 to the rest of list1
            prev.next = list1
        return head