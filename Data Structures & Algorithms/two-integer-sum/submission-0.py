class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for idx, num in enumerate(nums):
            if target - num not in s:
                s[num] = idx
            else:
                return [s[target-num], idx]
        return []