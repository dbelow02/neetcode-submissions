# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #This is just the is equal binary tree problem, but always return true if any true shows up
        #Could check if equal at each level
        if root is None and subRoot is None:
            return True
        if root is None:
            return False
        if self.dfs(root, subRoot):
            return True
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return (left or right)

    
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