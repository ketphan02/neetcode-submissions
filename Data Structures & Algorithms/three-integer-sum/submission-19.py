from collections import deque
from bisect import bisect_left

class Solution:
    def twoSum(self, nums: List[int], start: int) -> List[List[int]]:
        res = []
        l, r = start + 1, len(nums) - 1
        while l < r:
            cur_v = nums[l] + nums[r] + nums[start]
            if cur_v == 0:
                res.append((nums[start], nums[l], nums[r]))
                r -= 1
                l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
            elif cur_v > 0:
                r -= 1
            else:
                l += 1
        
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx - 1] == nums[idx]:
                continue
            res += self.twoSum(nums, idx)

        return res