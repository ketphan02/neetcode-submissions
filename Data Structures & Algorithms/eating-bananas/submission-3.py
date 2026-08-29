import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k):
            total = 0
            for b in piles:
                total += math.ceil(b / k)
                if total > h:
                    return False
            return True
    
        piles.sort()
        l, r = 1, piles[-1]
        while l < r:
            m = (l + r) // 2
            if not can_finish(m):
                l = m + 1
            else:
                r = m
        return l