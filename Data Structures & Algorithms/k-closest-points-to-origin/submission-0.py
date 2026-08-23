from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for point in points:
            x, y = point
            d = math.sqrt(x*x+y*y)
            heappush(h, (-d, [x, y]))
            while len(h) > k:
                heappop(h)
            
        return [x[1] for x in h]