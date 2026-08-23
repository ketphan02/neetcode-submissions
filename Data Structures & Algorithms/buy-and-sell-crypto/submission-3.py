class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_alltime = float('inf')

        for price in prices:
            min_alltime = min(min_alltime, price)
            res = max(res, price - min_alltime)

        return res
