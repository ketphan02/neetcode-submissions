import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeEatBananas(k):
            res = 0
            for pile in piles:
                res += math.ceil(float(pile) / k)
            return res

        piles.sort()

        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2
            if timeEatBananas(m) <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res