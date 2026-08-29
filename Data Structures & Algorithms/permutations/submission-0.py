class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def dfs(cur, available):
            if len(available) == 0:
                res.append(cur)
                return

            for num in available:
                dfs(cur + [num], available - {num})
        
        dfs([], set(nums))
        return res

            
            