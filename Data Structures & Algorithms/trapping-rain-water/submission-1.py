from collections import deque

class Solution:
    def trap(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            print(res, l, r)
            pending = 0
            if heights[l] <= heights[r]:
                next_l = l + 1
                while next_l < r and heights[next_l] <= heights[l]:
                    pending += heights[next_l]
                    next_l += 1
                area = (next_l - l - 1) * heights[l]
                l = next_l
            else:
                next_r = r - 1
                while next_r > l and heights[next_r] <= heights[r]:
                    pending += heights[next_r]
                    next_r -= 1
                area = (r - next_r - 1) * heights[r]
                r = next_r
            res += area - pending
        return res