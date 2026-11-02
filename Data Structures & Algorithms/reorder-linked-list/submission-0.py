# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Confused by the shuffle technique.
        #We assign an index to each node
        #Pairs of 0->n-1, 1->n-2, 2->n-3
        #Since single linked, it's difficult to traverse backwards efficiently.
        #We also don't know what n is, only our next.
        #Want O(n) time and O(1) space, so cannot loop over linked list multiple times. Figure out how
        #Create two halves?
        #Then, iterate over the two halves
        #Figure out where half is.
        if head is None:
            return 
        if head.next is None:
            return 
        n = 0
        next = head
        top = head
        while next is not None:
            n+=1
            next = next.next
        #Now, split into 2 lists
        mid = n // 2
        n = 0
        half1 = head
        half2 = head
        prev = half2
        while n != mid:
            #Get half2 start and break half1 from referencing half2
            prev = half2
            half2 = half2.next
            n+=1
        prev.next = None
        #Now have the two halves.
        #Reverse halve 2:
        prev = None
        while half2 is not None:
            next = half2.next
            half2.next = prev
            prev = half2
            half2 = next
        half2 = prev
        #len(half1) <= len(half2)
        #ie. half1 will always run out before half2
        while half1 is not None:
            nexthalf1 = half1.next
            nexthalf2 = half2.next
            half1.next = half2
            if nexthalf1 is not None:
                half2.next = nexthalf1
            else:
                if nexthalf2 is not None:
                    half2.next = nexthalf2
            half1 = nexthalf1
            half2 = nexthalf2
        #Half 2 is either none or already correctly connected.
        



