class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Best solution would be O(n) time, O(n) space.
        uniquenums = set(nums)
        return len(nums) != len(uniquenums)