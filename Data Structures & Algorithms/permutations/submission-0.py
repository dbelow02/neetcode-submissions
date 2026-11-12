class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #Slightly different than combination problem
        #Len must be the same as nums input
        #Question now becomes instead of do we keep this int
        #Does this int go in slot 1?
        #Two cases, yes, no.
        #Iterate through and append to results when run out of candidates.. or when len() == len(nums) - should be same.
        result = []

        def dfs(curlist, curpermutation):
            if len(curlist) == 0:
                result.append(list(curpermutation))
                return
            #Need to choose which elt goes in next slot
            for i in range(len(curlist)):
                #curlist[:i] + curlist[i+1:]
                curpermutation.append(curlist[i])
                dfs(curlist[:i] + curlist[i+1:], curpermutation)
                curpermutation.pop()
            
        dfs(nums, [])
        return result