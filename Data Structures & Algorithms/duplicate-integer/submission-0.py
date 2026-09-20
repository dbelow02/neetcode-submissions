class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Best solution would be O(n) time, O(n) space.


        #Most basic solution would be as follows,
        #However this is not optimal.
        lib = {}
        for num in nums:
            if num in lib.keys():
                return True
            lib[num] = 1
        return False