class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Min banana eaten would just be 1
        #Max is the max in piles (can't go any faster)
        #So then, just binary search to the min num that fits in h
        #O(nlogm) - logm for binary search, n for checking eating
        #How do we know if k is the correct one? Check for +1,-1?
        lowk = 1
        highk = max(piles)
        while lowk != highk:
            #Check if we can eat the bananas:
            mid = (lowk+highk)//2
            count = 0
            for pile in piles:
                #Ceil division:
                count += -(-pile // mid)
            if count <= h:
                #We did it! Is this the min?
                if mid == min(piles):
                    #yep
                    return mid
                #Check if mid-1 can do it.
                mid -= 1
                count = 0
                for pile in piles:
                    #Ceil division:
                    count += -(-pile // mid)
                if count <= h:
                    highk = mid
                    #We can still go lower.
                else:
                    #Nope, this is the min!
                    return mid + 1
            else:
                #We couldn't do it. Increase our eating rate
                lowk = mid + 1
        return highk
