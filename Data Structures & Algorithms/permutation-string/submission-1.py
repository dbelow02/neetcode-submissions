class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Sliding window
        #Keep dict of counts
        #Once count too big, move left until letter in conflict is cleared
        targetcounts = {}
        curcounts = {}
        for i in s1:
            targetcounts[i] = targetcounts.get(i,0) + 1
            #Populate the target char -> count dict
        left = 0
        for right in range(len(s2)):
            if curcounts == targetcounts:
                return True
            elif curcounts.get(s2[right], 0) < targetcounts.get(s2[right], 0):
                #increment and iterate right
                curcounts[s2[right]] = curcounts.get(s2[right], 0) + 1
            else: #have a conflict on letter s2[right]
                curcounts[s2[right]] = curcounts.get(s2[right], 0) + 1
                while curcounts.get(s2[right], 0) > targetcounts.get(s2[right],0):
                    curcounts[s2[left]] -= 1
                    if curcounts[s2[left]] == 0:
                        del curcounts[s2[left]]
                    left += 1
        return curcounts == targetcounts