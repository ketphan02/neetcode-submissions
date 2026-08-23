class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, num in enumerate(nums):
            if num > 0:
                return res
            
            if idx > 0 and num == nums[idx - 1]:
                continue
            
            l, r = idx + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + num < 0:
                    l += 1
                elif nums[l] + nums[r] + num > 0:
                    r -= 1
                elif nums[l] + nums[r] + num == 0:
                    res.append([nums[idx], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res