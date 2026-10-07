class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #O(N) time, O(1) space.
        minprice = 101
        maxprofit = 0
        for price in prices:
            if price < minprice:
                minprice = price
                continue
            if price - minprice > maxprofit:
                maxprofit = price-minprice
        return maxprofit