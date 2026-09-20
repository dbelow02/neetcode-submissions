class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Can do this naively by doing a total product, then a second pass where divide by nums[i]
        totalproduct = 1
        zeroproduct = 1
        countzero = 0
        for num in nums:
                if num == 0:
                    totalproduct = totalproduct * num
                    countzero += 1
                else:
                    totalproduct = totalproduct * num
                    zeroproduct = zeroproduct * num
        if countzero >= 2:
            for i in range(len(nums)):
                nums[i] = 0
        else:
            for i, num in enumerate(nums):
                if num == 0:
                    nums[i] = int(zeroproduct)
                else:
                    nums[i] = int(totalproduct / nums[i])
        return nums