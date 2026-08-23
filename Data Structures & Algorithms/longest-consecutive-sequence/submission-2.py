class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        res = 0
        for num in nums:
            if num not in s:
                continue
            
            cnt = 1
            lower, higher = num - 1, num + 1
            while lower in s:
                s.remove(lower)
                cnt += 1
                lower -= 1
            while higher in s:
                s.remove(higher)
                cnt += 1
                higher += 1

            res = max(res, cnt)
        return res