class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat_time(rate):
            res = 0
            for pile in piles:
                res += math.ceil(pile / rate)
            return res
        
        l, r = 1, max(piles) + 1
        while l < r:
            rate = (l + r) // 2
            if eat_time(rate) > h:
                l = rate + 1
            else:
                r = rate
        return l