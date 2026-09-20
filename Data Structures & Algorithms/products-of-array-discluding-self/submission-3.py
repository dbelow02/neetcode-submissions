class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Generate prefix array (left[i] = product of all to left)
        left = [0] * len(nums)
        for i in range(len(left)):
            if i == 0:
                left[i] = nums[i]
            else:
                left[i] = left[i-1] * nums[i]
        #Generate prefix array (right[i] = product of all to right)
        right = [0] * len(nums)
        for i in range(len(left)-1,-1,-1):
            if i == len(left)-1:
                right[i] = nums[i]
            else:
                right[i] = right[i+1] * nums[i]
        #Populate output array. out[i] = left[i-1] * right[i+1]
        for i in range(len(nums)):
            if i == 0:
                nums[i] = right[i+1]
            elif i == len(nums)-1:
                nums[i] = left[i-1]
            else:
                nums[i] = left[i-1] * right[i+1]
        return nums