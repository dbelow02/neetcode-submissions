class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #DFS backtracking
        #Decision is use above, below, left, right
        #Keep track of letters as soon as find first letter
        #Keeping track is the more difficult part.
        #Loop until find first letter?
        #Try without this check.

        def dfs(curPath, target):
            #Still looking for letters
            #Check if curPath[-1] is valid (not alr visited)
            #Optional: we don't actually care about the order
            #Just if it already exists. Swap curPath to a set.
            #For O(1) lookup instead of O(n)
            if curPath[-1] in curPath[:-1]:
                return False
            #Are we the target?
            if board[curPath[-1][0]][curPath[-1][1]] == word[target]:
                if target+1 == len(word):
                    #At the end of word!
                    return True
                #We are! Increment target and continue search
                #Need to try above, below, left, right
                #Up is i-1
                #Down is i+1
                #left is j-1
                #Right is j+1
                #Can also only visit if we haven't already visited!
                i,j = curPath[-1]
                if i-1 >= 0:
                    curPath.append((i-1,j))
                    up = dfs(curPath,target+1)
                    if up:
                        return True
                    curPath.pop()
                if i+1 < len(board):
                    curPath.append((i+1,j))
                    down = dfs(curPath,target+1)
                    if down:
                        return True
                    curPath.pop()
                if j-1 >= 0:
                    curPath.append((i,j-1))
                    left = dfs(curPath, target+1)
                    if left:
                        return True
                    curPath.pop()
                if j+1 < len(board[i]):
                    curPath.append((i,j+1))
                    right = dfs(curPath, target+1)
                    if right:
                        return True
                    curPath.pop()
                return False
            else:
                #We aren't. Can't be this path!
                return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                #Find all potential starting points
                if board[i][j] == word[0]:
                    if dfs([(i,j)],0):
                        return True
        return False