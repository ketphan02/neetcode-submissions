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
        h = []
        for interval in intervals:
            if len(h) > 0 and h[0] <= interval.start:
                heappop(h)
            heappush(h, interval.end)

        return len(h)