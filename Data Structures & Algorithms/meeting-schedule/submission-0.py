"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        if self.start == other.start:
            return self.end <= other.end
        return self.start <= other.start

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort()
        for idx in range(len(intervals) - 1):
            cur_interval = intervals[idx]
            next_interval = intervals[idx + 1]
            if next_interval.start < cur_interval.end:
                return False
        return True



