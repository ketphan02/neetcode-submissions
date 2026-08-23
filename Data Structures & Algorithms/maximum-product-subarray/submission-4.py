class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pL = [num for num in nums]
        nL = [num for num in nums]
        res_p = float("-inf")
        res_n = float("-inf")
        if nums[0] > 0:
            pL[0] = nums[0]
        else:
            nL[0] = nums[0]

        for idx, num in enumerate(nums):
            if idx == 0:
                continue
            if num > 0:
                pL[idx] = max(pL[idx-1] * num, num)
                nL[idx] = nL[idx-1] * num if nL[idx-1] < 0 else num
            else:
                pL[idx] = nL[idx-1] * num if nL[idx-1] < 0 else num
                nL[idx] = min(pL[idx-1] * num, num)
            res_p = max(res_p, pL[idx])
            res_n = max(res_n, num)
        

        res_p = max(res_p, pL[idx])
        res_n = max(res_n, num)
        return res_p if res_p > 0 else res_n
        