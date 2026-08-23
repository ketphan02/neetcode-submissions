from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def backtrack(idx):
            if idx >= len(nums):
                return 0

            yes_rob = nums[idx] + backtrack(idx + 2)
            no_rob = backtrack(idx + 1)

            return max(yes_rob, no_rob)
        
        return backtrack(0)