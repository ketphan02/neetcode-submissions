class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def helper(idx=0, cur_count=0, cur = []):
            if idx >= len(nums):
                return
            
            if nums[idx] + cur_count > target:
                return

            if nums[idx] + cur_count == target:
                res.append(cur + [nums[idx]])
                return

            helper(idx + 1, cur_count, cur)
            helper(idx, cur_count + nums[idx], cur + [nums[idx]])

        helper()
        return list(res)