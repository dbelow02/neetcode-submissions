class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #This is basically the same as min in a rotated sorted array
        #Could just find the rotation via finding the min, then binary search from there for the target.
        #This is the most intuitive to me.
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
        #Low rotate is now = the minimum element's index in the array
        #We can use this to "unrotate" the array and do a regular binary search.
        #Now, 0 is lowrotate high is (lowrotate + len(nums)) % len(nums)
        #Just map them
        low = 0
        high = len(nums)-1

        while low != high:
            #Calculating the midpoint is difficult.
            mid = (low+high) // 2
            if nums[(mid+lowrotate) % len(nums)] == target:
                return (mid+lowrotate) % len(nums)
            if nums[(mid+lowrotate) % len(nums)] > target:
                high = mid
            else:
                low = mid + 1
        if nums[(low + lowrotate) % len(nums)] == target:
            return (low + lowrotate) % len(nums)
        return -1





