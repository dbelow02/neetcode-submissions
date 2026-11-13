class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #Backtracking moment!
        #We choose where to put a queen on a board
        #Spaces we can put queens narrows by where previous ones are
        #Compute valid spaces at each turn
        #Keep track of where queens are at each turn
        #Append if we can hit n
        #Back track if no valid spaces left
        #Return the string version of valid positions
        #This is such a fun problem
        #Board is n,n
        positions = []


        #This solution works, but is too slow.
        #Rewrite to not need coveredSquares
        #Instead, incrementally keep a set of covered squares


        def coveredSquares(squares, queen, n):
            #already blocked squares, new queen, n
            #Block off vertical, then horizontal, then diagonal
            #make a copy:
            squares = set(squares)
            for i in range(n):
                squares.add((i, queen[1]))
            for i in range(n):
                squares.add((queen[0], i))
            for i in range(n):
                if queen[0] + i < n and queen[1] + i < n:
                    #down to the right
                    squares.add((queen[0]+i, queen[1]+i))
                if queen[0] - i >= 0 and queen[1] - i >= 0:
                    #up to the left
                    squares.add((queen[0]-i, queen[1]-i))
                if queen[0] - i >= 0 and queen[1] + i < n:
                    #up to the right
                    squares.add((queen[0]-i, queen[1]+i))
                if queen[0] + i < n and queen[1] - i >= 0:
                    #down to the left
                    squares.add((queen[0]+i, queen[1]-i))
                    
            return squares

        def dfs(squares, queens, n):
            if len(queens) == n:
                positions.append(list(queens))
                return
            #Can place a queen in any legal spot on the board
            #Get covered spots in order to know legal spots
            #In order to limit duplicates, place a queen at any available column in the next row.
            i = len(queens) #Must be a queen on each row
            #If let iterate over i,j end up with repeats based on ordering
            for j in range(n):
                if (i,j) not in squares:
                    #We can explore this path!
                    queens.append((i,j))
                    newsquares = coveredSquares(squares, (i,j), n)
                    dfs(newsquares, queens, n)
                    queens.pop()
            return
        
        dfs(set(), [], n)
        #Now positions is full of a list of pairs of queens. Construct output positions
        out = []
        for position in positions:
            #position is a list of queen positions
            board = []
            for i in range(n):
                row = ""
                for j in range(n):
                    foundqueen = False
                    for queen in position:
                        if i == queen[0] and j == queen[1]:
                            foundqueen = True
                            break
                    if foundqueen:
                        row += "Q"
                    else:
                        row += "."
                board.append(row)
            out.append(list(board))
        return out
        