class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for idx, num in enumerate(nums):
            if target - num in s:
                return [s[target - num], idx]
            s[num] = idx
        