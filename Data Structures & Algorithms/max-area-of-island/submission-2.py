class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #This is another dfs with visited style problem
        #Now, instead of keeping track of count of islands,
        #We count how large they are.

        maxArea = 0
        visited = set()
        stack = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    #Haven't seen this island yet, explore!
                    stack.append((i,j))
                    visited.add((i,j))
                    localArea = 0
                    while len(stack) > 0:
                        localArea += 1
                        coords = stack.pop()
                        h = coords[0]
                        k = coords[1]
                        #left, right, up, down
                        if h-1 >= 0 and (h-1,k) not in visited:
                            if grid[h-1][k] == 1:
                                stack.append((h-1,k))
                                visited.add((h-1,k))
                        if h+1 < len(grid) and (h+1,k) not in visited:
                            if grid[h+1][k] == 1:
                                stack.append((h+1,k))
                                visited.add((h+1,k))
                        if k-1 >= 0 and (h,k-1) not in visited:
                            if grid[h][k-1] == 1:
                                stack.append((h,k-1))
                                visited.add((h,k-1))
                        if k+1 < len(grid[0]) and (h,k+1) not in visited:
                            if grid[h][k+1] == 1:
                                stack.append((h,k+1))
                                visited.add((h,k+1))
                    maxArea = max(localArea, maxArea)
        return maxArea

