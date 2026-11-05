# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #oooo this is an interesting one
        #first must find p and q. Then traverse upwards until =
        #can we just increment p and q upwards each time?
        #Would require traversal down to p and q rather than bottom up
        if root is None:
            #At the bottom, didn't find it.
            return None
        if root is p or root is q:
            #I am p or q, report back up as found
            return root
        #Not bottom, not p/q, continue traversal
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left is not None and right is not None:
            #Found both left and right below me
            #I am the LCA!
            return root
        if left is not None:
            #Found left, report it up
            return left
        if right is not None:
            #Found right, report it up
            return right
        return None


