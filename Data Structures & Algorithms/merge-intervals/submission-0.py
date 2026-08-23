class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()
        cur = intervals[0]
        res = []
        for idx in range(1, len(intervals)):
            start, end = intervals[idx]
            if start > cur[1]:
                res.append(cur)
                cur = intervals[idx]
            else:
                cur[0] = min(cur[0], start)
                cur[1] = max(cur[1], end)

        res.append(cur)
        return res