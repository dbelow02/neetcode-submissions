# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #1 is left most, 2 is 1 in to the right, 3 is their parent, and so on
        #Don't need to know how many nodes in the tree
        #But do need to go bottom up, I believe.
        #This is because we know left most is smallest
        #Then, can traverse upwards from here
        #Stack of left's parents?
        self.k = 0
        self.found = None
        self.dfs(root, k)
        return self.found
    def dfs(self, root, k):
        #traverses down left tree first, then figures out own position from this.
        if root is None or self.found is not None:
            #Parent must be bottom of subtree
            return
        #Check left, self, then right (in order of val size)
        #left < self < right
        self.dfs(root.left, k)
        self.k += 1
        if self.k == k:
            self.found = root.val
        self.dfs(root.right, k)
        return
        