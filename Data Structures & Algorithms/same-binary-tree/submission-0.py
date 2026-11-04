# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #A tree is only equal if left and right are also equal
        #And so on, until bottom
        #So, traverse to bottom and then evaluate.
        return self.dfs(p,q)
    def dfs(self, left: Optional[TreeNode], right: Optional[TreeNode]):
        # keep track of height and a bool
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        doubleleft = self.dfs(left.left,right.left)
        doubleright = self.dfs(left.right,right.right)
        return (doubleleft and doubleright)
        