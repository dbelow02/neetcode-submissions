class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #Just an index choose problem
        #How to implement choose function?
        #List choose 0, choose 1, choose 2, etc. Until n = len nums
        #Once choose n numbers together, at least 1 must be dif next
        #One list of subsets contains num and one does not
        #Backtracking?
        #Two cases - add index to cur list, and don't
        # = 2 recursive calls? Then append everything together?
        #Why need backtracking then?
        if len(nums) == 0:
            #Empty subset!
            return [[]]
        #recursively call self with nums in and nums out
        numout = self.subsets(nums[1:])
        #numout is list of list of int
        #add [nums[0]] to every elt (extend the list w/ nums[0])
        return numout + [[nums[0]] + x for x in numout]
        

        