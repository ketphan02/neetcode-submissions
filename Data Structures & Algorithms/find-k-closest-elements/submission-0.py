class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = []
        for v in arr:
            heapq.heappush(h, (abs(v - x), v))
        
        res = sorted([v[1] for v in heapq.nsmallest(k, h)])
        return res