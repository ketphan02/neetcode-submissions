class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cur = 1
        pre = []
        for num in nums:
            pre.append(cur)
            cur *= num

        post = 1
        for idx in range(len(nums) - 1, -1, -1):
            num = nums[idx]
            pre[idx] *= post
            post *= num
        
        return pre
