from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def solve(cur: int, idx: int) -> int:
            if idx >= len(s):
                return 1
            if cur == 0 and s[idx] == '0':
                return 0

            next_num = ord(s[idx]) - ord('0')
            new = cur * 10 + next_num

            res = 0
            if next_num != 0:
                res = solve(next_num, idx + 1)
            if 10 <= new and new <= 26:
                res += solve(0, idx + 1)
            return res
        
        return solve(0, 0)