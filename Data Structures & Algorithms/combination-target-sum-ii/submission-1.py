class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #Similar to combination sum problem
        #candidates may contain duplicates (ie multiple 1's)
        #Now, the include / exclude becomes not just moving index 1
        #But moving index past all duplicates
        result = []
        candidates = sorted(candidates)
        
        def dfs(index, curlist, cursum):
            if cursum == target:
                result.append(list(curlist))
                return
            if index >= len(candidates) or cursum > target:
                return
            #Two cases, we use this number
            #We don't
            curlist.append(candidates[index])
            #Can still use duplicates in this case
            dfs(index+1, curlist, cursum + candidates[index])
            curlist.pop()
            #Cannot use duplicates here (would result in duplicate subsets)
            #Increment index until candidates[index] != num
            num = candidates[index]
            while index < len(candidates):
                #Search for num
                if candidates[index] == num:
                    #keep going
                    index += 1
                else:
                    break
            dfs(index, curlist, cursum)
            return

        dfs(0,[],0)
        return result
