# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]
        #Did brute force, now try optimally!
        #Can we do it DFS/ BFS?
        #Compute at each level going up instead of down.
    def dfs(self, root:Optional[TreeNode]) -> bool:
        #Keep track of whether or not balanced, and height at each node.
        if root is None:
            return [True,0]
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
            return [True, 1 + max(left[1], right[1])]
        return [False, 1 + max(left[1], right[1])]
        