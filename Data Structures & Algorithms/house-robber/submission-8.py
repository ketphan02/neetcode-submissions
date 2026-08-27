from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        

        @cache
        def rob_backtrack(idx):
            if idx >= len(nums):
                return 0
            return max(rob_backtrack(idx + 1), rob_backtrack(idx + 2) + nums[idx])
        
        if len(nums) <= 2:
            return max(nums)

        nums[1] = max(nums[0], nums[1])

        for idx in range(2, len(nums)):
            nums[idx] = max(nums[idx - 2] + nums[idx], nums[idx - 1])
        return nums[-1]