class Solution:
    def trap(self, height: List[int]) -> int:
        #O(n) time and O(n) space means we must be pruning the solution space at each step
        #Likely a two pointer and a hashing problem
        #Try to figure out a clever hashing method that makes it so we know how much water is stored at each step and what we're looking for to break it.
        #Amount of water at i can be calculated by left (where left is the nearest wall to the left), and right (where right is the nearest wall to the right) we can use this to get min(height[left], height[right]) - height[i]
        #Determining the correct right and left is the challenge.
        #can track the max from prefix/suffix in an array.
        maxprefix = [0] * len(height)
        maxleft = 0
        for i in range(len(height)):
            maxprefix[i] = maxleft
            if height[i] > maxleft:
                maxleft = height[i]
        maxsuffix = [0] * len(height)
        maxright = 0
        for i in range(len(height)-1, 0, -1):
            maxsuffix[i] = maxright
            if height[i] > maxright:
                maxright = height[i]

        #Now have max suffix and prefix, do a final trip over
        water = 0
        for i in range(len(height)):
            water += max(0,min(maxprefix[i], maxsuffix[i]) - height[i])
        return water

