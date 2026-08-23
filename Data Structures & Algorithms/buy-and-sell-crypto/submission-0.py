class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = prices[:]
        for i in range(len(prices) - 2, -1, -1):
            L[i] = max(L[i], L[i + 1])
        res = 0
        for i in range(len(prices)):
            res = max(res, L[i] - prices[i])
        return res