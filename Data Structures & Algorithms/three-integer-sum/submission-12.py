from collections import deque
from bisect import bisect_left

class Solution:
    def twoSum(self, nums: List[int], start: int) -> List[List[int]]:
        target = -nums[start]

        res = []
        for idx in range(start + 1, len(nums)):
            k = target - nums[idx]
            found_idx = bisect_left(nums, k, lo=idx+1)
            if found_idx < 1 or found_idx >= len(nums):
                continue
            if nums[found_idx] == k:
                res.append([-target, nums[idx], k])
        
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for idx in range(len(nums) - 2):
            res += self.twoSum(nums, idx)
            while 1 <= idx and idx < len(nums) and nums[idx - 1] == nums[idx]:
                idx += 1

        return [list(n) for n in set(map(tuple, res))]