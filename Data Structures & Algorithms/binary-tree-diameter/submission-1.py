# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #This is a weird one, how do we do it?
        #Can do recursively? Would need to keep track of current max.
        #Can do that with a global I guess.
        #Need to take a break from coding for a while.
        self.maxWidth = 0
        self.getBinaryTreeDepth(root)
        return self.maxWidth
        
    def getBinaryTreeDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftdepth = self.getBinaryTreeDepth(root.left)
        rightdepth = self.getBinaryTreeDepth(root.right)
        self.maxWidth = max(self.maxWidth, leftdepth+rightdepth) #this is the trick, checking all throughout the tree if width is greater.
        return 1 + max(leftdepth,rightdepth)