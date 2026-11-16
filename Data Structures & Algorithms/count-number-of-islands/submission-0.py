class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Lol this was a problem for EECS281 I think
        #Challenge is that it is difficult to find the edges of an island
        #DFS?
        #want O(m*n) time and space
        #Think it is just a dfs with marking islands as visited.
        #Use a stack to keep track of islands?
        visited = set() #use this to track visited land coords
        #Start from each point on the grid
        count = 0
        stack = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    #Found land, have we already visited?
                    #Increment counter and explore!
                    count += 1
                    #Fill out stack, then loop.
                    #left, right, up, down
                    if i-1 >= 0:
                        if grid[i-1][j] == "1":
                            stack.append((i-1,j))
                    if i+1 < len(grid):
                        if grid[i+1][j] == "1":
                            stack.append((i+1,j))
                    if j-1 >= 0:
                        if grid[i][j-1] == "1":
                            stack.append((i,j-1))
                    if j+1 < len(grid[0]):
                        if grid[i][j+1] == "1":
                            stack.append((i,j+1))
                    while len(stack) > 0:
                        #Visit the land!
                        coords = stack.pop()
                        visited.add(coords)
                        h = coords[0]
                        k = coords[1]
                        if h-1 >= 0 and (h-1,k) not in visited:
                            if grid[h-1][k] == "1":
                                stack.append((h-1,k))
                        if h+1 < len(grid) and (h+1,k) not in visited:
                            if grid[h+1][k] == "1":
                                stack.append((h+1,k))
                        if k-1 >= 0 and (h,k-1) not in visited:
                            if grid[h][k-1] == "1":
                                stack.append((h,k-1))
                        if k+1 < len(grid[0]) and (h,k+1) not in visited:
                            if grid[h][k+1] == "1":
                                stack.append((h,k+1))

                #Otherwise, we keep on chugging
        return count