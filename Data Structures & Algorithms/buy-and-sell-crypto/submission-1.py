class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        res = float("-inf")
        for price in prices:
            min_price = min(min_price, price)
            res = max(res, price - min_price)
            
        return res