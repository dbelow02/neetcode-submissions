class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Interesting, how do we "unrotate"
        #Do we need to?
        #Figure out how rotated it is, then binary search?
        #Max N/2 rotations possible
        #If we know how it is rotated, we know where index 0 now lies.
        #Can binary search through rotated possibilities
        #We know is rotated less if next elt < own
        #We know is rotated more if next elt > own
        #Else, min!

        lowrotate = 0
        highrotate = len(nums)-1
        while lowrotate != highrotate:
            mid = (lowrotate + highrotate) // 2
            #Compare to high as if less than high, we know between mid and high is sorted
            #Thus, it must be to the left (high now = mid)
            if nums[mid] < nums[highrotate]:
                highrotate = mid
            else: 
                lowrotate = mid + 1
        return nums[lowrotate]
        

