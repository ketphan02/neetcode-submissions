from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.max_h = []
        self.min_h = []

    def _move_head(self, from_heap, to_heap):
        top = heappop(from_heap)
        heappush(to_heap, -top)
    
    def addNum(self, num: int) -> None:
        if not self.max_h:
            heappush(self.max_h, -num)
        elif not self.min_h and num > -self.max_h[0]:
            heappush(self.min_h, num)
        elif len(self.max_h) == len(self.min_h):
            if num > self.min_h[0]:
                self._move_head(from_heap=self.min_h, to_heap=self.max_h)
                heappush(self.min_h, num)
            else:
                heappush(self.max_h, -num)
        else:
            if num < -self.max_h[0]:
                self._move_head(from_heap=self.max_h, to_heap=self.min_h)
                heappush(self.max_h, -num)
            else:
                heappush(self.min_h, num)


    def findMedian(self) -> float:
        if len(self.max_h) == len(self.min_h):
            return float(-self.max_h[0] + self.min_h[0]) / 2.0
        return -self.max_h[0]
        