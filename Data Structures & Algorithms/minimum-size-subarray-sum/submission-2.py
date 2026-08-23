class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        cur_sum = 0
        res = float('inf')
        while r < len(nums):
            cur_sum += nums[r]
            while l <= r and cur_sum >= target:
                res = min(res, r - l + 1)
                cur_sum -= nums[l]
                l += 1
            r += 1
            
        return res if res != float('inf') else 0