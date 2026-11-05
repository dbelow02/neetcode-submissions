# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Essentially asking to find the right most node at each level
        #Priority is checking right side first
        #Is the right most if an entry doesn't already exist for that level
        #Again, can use an external list / dict to keep track of level info
        #Checking right side first guarantees we find rightmost first
        #Each node checks if level already exists at that level
        #If no, I am the right most
        #If not, check children (right first)
        self.rightmost = {}
        self.checkRightMost(root, 0)
        return [self.rightmost[x] for x in self.rightmost]

    
    def checkRightMost(self, root, level):
        if root is None:
            return
        if self.rightmost.get(level,-101) == -101:
            #I am the most right!
            self.rightmost[level] = root.val
        self.checkRightMost(root.right, level + 1)
        self.checkRightMost(root.left, level + 1)
        return
