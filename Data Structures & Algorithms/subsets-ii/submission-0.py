class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Is this not the same as combination sum but without sum part?
        #Just include or don't include..

        result = []
        #Need sorted so don't do duplicates when don't include.
        sortednums = sorted(nums)

        def dfs(index, curperm):
            if index >= len(sortednums):
                result.append(list(curperm))
                return
            #Include!
            curperm.append(sortednums[index])
            dfs(index+1, curperm)
            #Don't include!
            curperm.pop()
            #Find next non-duplicate.
            num = sortednums[index]
            while index < len(nums):
                if sortednums[index] == num:
                    index += 1
                else:
                    break
            dfs(index, curperm)
            return
        
        dfs(0, [])
        return result
