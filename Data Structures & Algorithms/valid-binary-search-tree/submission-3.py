# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Solution currently only checks left/right values, not ancestors
    #For instance, 0 at root, -1000 left, 1000 right, -10 left child on right would return valid. However, this left child on right should be on the left side as it is less than the parent
    #Need to include these checks. 
    #left, left and right, right by default covered
    #left, right and right, left still need to be covered.

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #Can iterate down tree and check vals at each level
        #Return true/false
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, root, low, high):
        if root is None:
            return True
        if not (low < root.val < high):
            return False
        return self.dfs(root.left, low, root.val) and self.dfs(root.right, root.val, high)
