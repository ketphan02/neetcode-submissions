from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for i in range(len(nums)):
            a, b = b, max(b, nums[i] + a)
        return b