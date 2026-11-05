# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #Can do this via keeping track of max value in current path
        #Then, if good node, propogate back up
        #So, each node checks if own value > than previous max
        #If greater, swaps previous max
        #Is good node, count = 1
        #Call children
        #Add any children good nodes found.
        return self.isGoodNode(root, -101)

    def isGoodNode(self, root, maxVal):
        #Takes root, maxVal seen, returns int of how many good nodes below this one
        if root is None:
            return 0
        if root.val >= maxVal:
            #This root is a good node, update maxval
            return 1 + self.isGoodNode(root.left, root.val) + self.isGoodNode(root.right, root.val)
        #Root was not good node, keep working down
        return self.isGoodNode(root.left, maxVal) + self.isGoodNode(root.right, maxVal)


