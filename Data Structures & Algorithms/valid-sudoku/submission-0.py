class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Could easily do this in O(n^2)
        #Check rows, check columns, check sums.

        #Likely a compliments type problem
        #Board does not need to be solvable to be valid,
        #Just cannot be invalid.
        #Row1 still requires 4-9
        #Col1 still requires 2,3,6,8,9
        #Cube 1 still requires 3,5,6,7
        #Can we verify if this 

        #Going to be set math with compliments.
        #Verify cube works with columns, then cube with rows.
        #Cube 1 still requires 3,5,6,7

        #Consider row/col: potential options = row options union column
        #Then for 3x3, add in this union. If any are none, it is invalid. Can solve by recursing if want to solve.

        #Populate compliments, then check if valid. This decides if is solvable. Don't need to decide if solvable, just valid.
        row = [set() for _ in range(9)] #list of sets.
        col = [set() for _ in range(9)]
        cube = [set() for _ in range(9)]
        for i in range(9): #row
            for j in range(9): #col
                #Check board init
                cubeindex = (i // 3) * 3 + (j // 3) #0->8
                if board[i][j] == ".":
                    continue
                #Now, check for duplicates.
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in cube[cubeindex]:
                    return False
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    cube[cubeindex].add(board[i][j])
        return True
