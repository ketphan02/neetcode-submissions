class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for idx, h in enumerate(heights + [0]):
            cur_idx = idx
            while len(stack) > 0 and stack[-1][0] > h:
                top_h, top_idx = stack.pop()
                res = max(res, top_h * (idx - top_idx))
                cur_idx = top_idx
            stack.append((h, cur_idx))
        
        return res
            
