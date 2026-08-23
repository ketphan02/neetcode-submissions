class MedianFinder:

    def __init__(self):
        self.l = []
        self.r = []

    def addNum(self, num: int) -> None:
        if not self.l:
            heapq.heappush(self.l, -num)
        elif num <= -self.l[0]:
            heapq.heappush(self.l, -num)
            if len(self.l) - 1 > len(self.r):
                top = heapq.heappop(self.l)
                heapq.heappush(self.r, -top)
        else:
            heapq.heappush(self.r, num)
            if len(self.r) - 1 > len(self.l):
                top = heapq.heappop(self.r)
                heapq.heappush(self.l, -top)


    def findMedian(self) -> float:
        print(self.l, self.r)
        if len(self.l) > len(self.r) or not self.r:
            return -self.l[0]
        
        if len(self.l) == len(self.r):
            return (-self.l[0] + self.r[0]) / 2.0

        return self.r[0]