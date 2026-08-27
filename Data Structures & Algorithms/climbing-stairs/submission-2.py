from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def backtrack(num_left):
            if num_left == 0:
                return 1
            if num_left < 0:
                return 0
            
            return backtrack(num_left - 1) + backtrack(num_left - 2)


        L = [0 for _ in range(n + 1)]
        L[n] = 1
        for i in range(n, -1, -1):
            k = i - 1
            if k >= 0:
                L[k] += L[i]
            k = i - 2
            if k >= 0:
                L[k] += L[i]
        return L[0]

