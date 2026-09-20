class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Classic trick for two some is store the compliment.
        #Good lesson for future problems.
        #Don't necessarily need to store the number, just what you
        #learned from said number

        targets = {}
        for i,num in enumerate(nums):
            if num in targets.keys():
                return [targets[num], i]
            targets[target-num] = i
        return 0