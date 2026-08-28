from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robber(nums):
            a, b = 0, 0
            for num in nums:
                a, b = b, max(b, a + num)
            return b
        
        if len(nums) <= 2:
            return max(nums)
        return max(robber(nums[1:]), robber(nums[:-1]))