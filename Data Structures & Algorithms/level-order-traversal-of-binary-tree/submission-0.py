# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Interesting, will need to know the level of each node
        #Keep a global dict of level?
        #Each node processes itself, in addition to it's children.
        #Then, can process the dict afterwards into output format.
        #Each iteration will need root, and its previous level
        #It will not return anything, but populate a dict
        #Calls left and right to do the same 
        self.levels = {}
        self.appendLevel(root, 0)
        #Now we have self.levels populated. Iterate through and return!
        out = [self.levels[x] for x in self.levels]
        return out
    
    def appendLevel(self, root, level):
        if root is None:
            return
        levellist = self.levels.get(level, list())
        levellist.append(root.val)
        self.levels[level] = levellist
        #Awesome, we appended ourselves at the correct depth, now traverse deeper!
        self.appendLevel(root.left, level+1)
        self.appendLevel(root.right, level+1)
        return
