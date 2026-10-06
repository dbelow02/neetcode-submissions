class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Trick to two pointer problems is finding a sorting / contraction mechanism that shrinks the input space at every move without being greedy. For example I originally tried solution here with left and right pointers being assigned at the tallest 2 objects, then expanding outwards based on maxwater either direction. However, this is greedy and potentially misses global optimum
        #Must be able to prove that is not greedy in order to be good solution
        #We move left/right because found upper bound with whichever pointer we choose to move.
        #In this case, we move the shorter one as it is upper bounded by the shortest height, and any step inwards cannot increase the water volume. (monotonically decreasing from the moved pointer)
        left = 0
        right = len(heights) - 1
        maxWater = -500
        while right-left >= 1:
            if min(heights[left], heights[right]) * (right - left) > maxWater:
                maxWater = min(heights[left], heights[right]) * (right - left)
            #Now, move the pointers
            #Ties broken arbitrarily (both bounded)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxWater