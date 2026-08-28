from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        nums[1] = max(nums[0], nums[1])
        a, b = nums[0], max(nums[1], nums[0])
        for i in range(2, len(nums)):
            tmp = b
            b = max(b, nums[i] + a)
            a = tmp
        return b