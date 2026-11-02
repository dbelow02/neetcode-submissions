class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #This is just a 2D binary search. 1 for row, then for col.
        #Find the row:
        lowrow = 0
        highrow = len(matrix)
        row = None
        while lowrow != highrow:
            mid = (lowrow+highrow)//2
            #check around row.
            #If row correct, target should be > row - 1 and < row + 1
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row = mid
                break
            if matrix[mid][0] > target:
                highrow = mid
            else:
                lowrow = mid + 1
        if row is None:
            return False
        #Now, find the column. Just a normal binary search at this point
        lowcol = 0
        highcol = len(matrix[row])
        while lowcol != highcol:
            mid = (lowcol+highcol)//2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                highcol = mid
            else:
                lowcol = mid + 1
        return False