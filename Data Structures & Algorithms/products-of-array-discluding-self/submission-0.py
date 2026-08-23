class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        pre = []
        for num in nums:
            prefix *= num
            pre.append(prefix)
        postfix = 1
        post = [1 for _ in nums]
        for idx in range(len(nums) - 1, -1, -1):
            num = nums[idx]
            postfix *= num
            post[idx] = postfix

        
        res = []
        for idx in range(len(nums)):
            if idx == 0:
                res.append(post[idx + 1])
            elif idx == len(nums) - 1:
                res.append(pre[idx - 1])
            else:
                res.append(post[idx + 1] * pre[idx - 1])
        return res
