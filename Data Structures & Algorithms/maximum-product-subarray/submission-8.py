from functools import cache

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [num for num in nums]
        dp_min = [num for num in nums]

        res = nums[0]
        for idx in range(1, len(nums)):
            num = nums[idx]
            dp_max[idx] = max(num, num * dp_max[idx - 1], num * dp_min[idx - 1])
            dp_min[idx] = min(num, num * dp_max[idx - 1], num * dp_min[idx - 1])

            res = max(res, dp_max[idx])

        return res
