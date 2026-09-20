class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Best solution would be O(n) time, O(n) space.


        #Most basic solution would be as follows,
        #However this is not optimal. (should use a set instead of a dict)
        #Set stores only keys, not values (shouldn't store 1 on each..)
        lib = {}
        for num in nums:
            if num in lib.keys():
                return True
            lib[num] = 1
        return False