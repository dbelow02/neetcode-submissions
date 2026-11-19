# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #This is a fun one. 
        #Remember to carry your ones!
        #Will need to handle uneven l/r
        root = ListNode()
        node = root
        if l1 and l2:
            carry = 0
            while l1 or l2:
                if l1 and l2:
                    #Both, so add em!
                    val = l1.val + l2.val + carry
                    if val > 9:
                        carry = 1
                        newnode = ListNode()
                        newnode.val = val-10
                    else:
                        carry = 0
                        newnode = ListNode()
                        newnode.val = val
                    l1 = l1.next
                    l2 = l2.next
                    node.next = newnode
                    node = newnode
                elif l1:
                    val = l1.val + carry
                    if val > 9:
                        carry = 1
                        newnode = ListNode()
                        newnode.val = val-10
                    else:
                        carry = 0
                        newnode = ListNode()
                        newnode.val = val
                    l1 = l1.next
                    node.next = newnode
                    node = newnode
                else:
                    val = l2.val + carry
                    if val > 9:
                        carry = 1
                        newnode = ListNode()
                        newnode.val = val-10
                    else:
                        carry = 0
                        newnode = ListNode()
                        newnode.val = val
                    l2 = l2.next
                    node.next = newnode
                    node = newnode  
            if carry == 1:
                newnode = ListNode()
                newnode.val = 1
                node.next = newnode
                node = newnode

        elif not l1 and not l2:
            return None
        elif l1:
            return l1
        else:
            return l2
        return root.next