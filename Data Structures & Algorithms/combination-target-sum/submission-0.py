from functools import cache

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(nums, target, trace):
            if target == 0:
                res.append(trace)
                return
            if target < 0:
                return
            for idx, num in enumerate(nums):
                backtrack(nums[idx:], target - num, trace + [num])
        backtrack(nums, target, [])
        return res