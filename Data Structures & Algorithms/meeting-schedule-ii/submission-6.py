"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        heap = []
        for interval in intervals:
            if not heap:
                heappush(heap, interval.end)
            elif interval.start < heap[0]:
                heappush(heap, interval.end)
            else:
                heappop(heap)
                heappush(heap, interval.end)
        
        print(heap)
        return len(heap)



