class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = prices[0]
        for price in prices:
            minPrice = min(price, minPrice)
            curProfit = price - minPrice 
            res = max(res,curProfit)
        return res