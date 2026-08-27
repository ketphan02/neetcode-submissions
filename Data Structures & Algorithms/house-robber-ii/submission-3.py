from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def solve(nums):
            @cache
            def robbing(idx=0):
                if idx >= len(nums):
                    return 0
                
                return max(robbing(idx + 1), robbing(idx + 2) + nums[idx])
            
            return robbing()
        

        if len(nums) <= 2:
            return max(nums)
        return max(solve(nums[:-1]), solve(nums[1:]))