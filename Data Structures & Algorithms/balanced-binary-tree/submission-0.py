# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #Can just get height of all children
        #Have each return true. If any return false, everything returns false
        #Traverse tree and check at each level
        #Check if balanced at this level
        if root is None:
            return True
        if abs(self.getHeight(root.left) - self.getHeight(root.right)) > 1:
            return False
        else:
            return (self.isBalanced(root.left) and self.isBalanced(root.right))
    
    def getHeight(self, root:Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))