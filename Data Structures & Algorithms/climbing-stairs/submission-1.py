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

        return backtrack(n)

