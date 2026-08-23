class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        if intervals[0][0] > newInterval[1]:
            return [newInterval] + intervals

        i = -1
        n = len(intervals)
        while True:
            i += 1
            if i >= len(intervals):
                return intervals + [newInterval]
            
            print(i, intervals, newInterval)
            if intervals[i][1] < newInterval[0]:
                continue
            if intervals[i][0] <= newInterval[0] and newInterval[1] <= intervals[i][1]:
                return intervals
            if newInterval[0] <= intervals[i][0] and intervals[i][1] <= newInterval[1]:
                del intervals[i]
                i -= 1
            elif intervals[i][0] <= newInterval[0]:
                newInterval[0] = intervals[i][0]
                del intervals[i]
                i -= 1
            elif newInterval[0] <= intervals[i][0] <= newInterval[1]:
                intervals[i][0] = newInterval[0]
                return intervals
            elif newInterval[0] <= intervals[i][1] <= newInterval[1]:
                intervals[i][1] = newInterval[1]
                return intervals
            else:
                intervals.insert(i, newInterval)
                return intervals
