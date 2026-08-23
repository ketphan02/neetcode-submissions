class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums = [1] + nums + [1]
        res, l, r = [1 for _ in nums], [1 for _ in nums], [1 for _ in nums]

        for idx in range(1, len(nums)):
            l[idx] = nums[idx - 1] * l[idx - 1]
        for idx in range(len(nums) - 2, -1, -1):
            r[idx] = r[idx + 1] * nums[idx + 1]

        for idx in range(1, len(nums) - 1):
            res[idx] = l[idx] * r[idx]
        
        return res[1:][:-1]