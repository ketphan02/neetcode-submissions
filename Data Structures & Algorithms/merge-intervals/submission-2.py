class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort()
        res = []
        cur_interval = intervals[0]
        for interval in intervals[1:]:
            if cur_interval[0] <= interval[0] <= cur_interval[1]:
                cur_interval = [min(cur_interval[0], interval[0]), max(cur_interval[1], interval[1])]
            else:
                res.append(cur_interval)
                cur_interval = interval

        
        res.append(cur_interval)
        return res