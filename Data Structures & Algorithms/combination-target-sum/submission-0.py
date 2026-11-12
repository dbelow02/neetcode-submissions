class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #First instinct is hash?
        #Can either add a number to num or not.
        #Then, when we reach num, log as answer.
        #Hash table gets huge though something like O(2^n) space
        #O(n) time
        #Question instead wants linear space.
        #Could use dynamic programming potentially in this case
        #Keep sums in DP array
        #Then, hash what sum needed to hit target on combination
        #But, this is a backtracking problem
        #Struggle with backtracking logic tbh
        
        #Stop extending path when can't reach target
        #(All number give a sum > than, or numbers left is empty)
        #Have a choice at each. Use num or don't.
        out = []

        def dfs(index, curlist, cursum):
            if cursum == target:
                out.append(list(curlist))
                #Have to use list(curlist) because just curlist
                #Would append a reference, which gets changed
                #So, construct a new list that doesn't
                #Ever get touched
                #Finished exploring this path
                return
            if index >= len(nums) or cursum > target:
                #Can't be this path, finished exploring
                return
            #Two cases:
            #We include nums and recurse
            #We don't include nums and recurse
            curlist.append(nums[index]) #Append
            dfs(index, curlist, cursum+nums[index])
            #Now, remove for the second case.
            curlist.pop()
            dfs(index+1, curlist, cursum)
        
        dfs(0, [], 0)
        return out
