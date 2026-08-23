class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 in nums:
                continue
            l = 1
            while num + l in nums:
                l += 1
            res = max(l, res)
        return res