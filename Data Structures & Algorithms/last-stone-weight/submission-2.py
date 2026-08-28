from heapq import heapify, heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapify(stones)

        while len(stones) > 2:
            a, b = heappop(stones), heappop(stones)
            if a != b:
                heappush(stones, -abs(a - b))

        if len(stones) == 2:
            return abs(heappop(stones) - heappop(stones))
        if len(stones) == 1:
            return -heappop(stones)
        return 0