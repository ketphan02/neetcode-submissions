from functools import cache

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = nums[0]
        dp_min = nums[0]
        res = nums[0]
        for idx in range(1, len(nums)):
            num = nums[idx]
            next_max = max(num, num * dp_max, num * dp_min)
            next_min = min(num, num * dp_max, num * dp_min)

            res = max(res, next_max)

            dp_max = next_max
            dp_min = next_min

        return res
