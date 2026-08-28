import math
from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def d(point):
            return math.sqrt(point[0] * point[0] + point[1] * point[1])
        
        h = []
        for point in points:
            heappush(h, (-d(point), point))
            if len(h) > k:
                heappop(h)
        
        return list(map(lambda x: x[1], h))