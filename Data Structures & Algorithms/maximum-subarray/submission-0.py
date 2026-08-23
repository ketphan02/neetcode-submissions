class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        cur = 0
        for num in nums:
            cur += num
            res = max(res, cur)
            if cur < 0:
                cur = 0
            
        return res