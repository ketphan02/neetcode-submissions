from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        @cache
        def backtrack(idx, limit):
            if idx >= limit:
                return 0

            yes_rob = nums[idx] + backtrack(idx + 2, limit)
            no_rob = backtrack(idx + 1, limit)

            return max(yes_rob, no_rob)
        
        return max(backtrack(0, len(nums) - 1), backtrack(1, len(nums)))