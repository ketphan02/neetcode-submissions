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
            elif cur_v > 0:
                r -= 1
            else:
                l += 1
        
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for idx in range(len(nums) - 2):
            res += self.twoSum(nums, idx)
            while 1 <= idx and idx < len(nums) and nums[idx - 1] == nums[idx]:
                idx += 1

        return [list(n) for n in set(res)]