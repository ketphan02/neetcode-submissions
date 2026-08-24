class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []

        def helper(idx=0, cur_count=0):
            if cur_count == target:
                res.append(cur.copy())
                return

            if idx >= len(nums):
                return
            
            if nums[idx] + cur_count > target:
                return

            helper(idx + 1, cur_count)

            cur.append(nums[idx])
            helper(idx, cur_count + nums[idx])
            cur.pop()

        helper()
        return list(res)