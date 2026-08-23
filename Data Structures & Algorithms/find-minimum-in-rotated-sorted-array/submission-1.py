class Solution:
    def findMin(self, nums: List[int]) -> int:

        def find_head(l, r):
            if l >= r:
                return -1 # Everything is correct

            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                return m + 1
            if m > 0 and nums[m - 1] > nums[m]:
                return m
            l_search = find_head(l, m)
            r_search = find_head(m + 1, r)

            return max(l_search, r_search)
        
        res = find_head(0, len(nums) - 1)
        if find_head(0, len(nums) - 1) == -1:
            return nums[0]
        return nums[res]

            