from collections import deque
from bisect import bisect_left

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 2:
            return []

        res = []
        for idx in range(len(nums)):
            k = target - nums[idx]
            found_idx = bisect_left(nums, k, lo=idx+1, hi=len(nums))
            if found_idx < 1 or found_idx >= len(nums):
                continue
            if nums[found_idx] == k:
                res.append([-target, nums[idx], k])
        
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums = deque(nums)

        res = []
        while len(nums):
            cur = nums.popleft()
            res += self.twoSum(nums, -cur)

        return [list(x) for x in set(map(tuple, res))]