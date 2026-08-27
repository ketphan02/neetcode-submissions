from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        

        @cache
        def rob_backtrack(idx):
            if idx >= len(nums):
                return 0
            return max(rob_backtrack(idx + 1), rob_backtrack(idx + 2) + nums[idx])
        
        return rob_backtrack(0)