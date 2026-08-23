class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for k in range(n):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            l, r = k + 1, n - 1
            while l < r:
                if nums[l] + nums[r] + nums[k] == 0:
                    res.append([nums[k], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] + nums[k] > 0:
                    r -= 1
                else:
                    l += 1
        return res