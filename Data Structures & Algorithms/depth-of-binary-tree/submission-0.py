# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #O(n) time, O(n) space.
        #My gut is to just do it recursively.
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is not None and root.right is not None:
            return 1 + max(self.maxDepth(root.right),self.maxDepth(root.left))
        if root.left is not None:
            #right is none
            return 1 + self.maxDepth(root.left)
        else:
            #left is none
            return 1 + self.maxDepth(root.right)
        