from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        valid_c = set(str(i) for i in range(1, 27))

        @cache
        def solve(cur: str, idx: int) -> int:
            if cur == "0":
                return 0
            if idx >= len(s):
                return 1
            
            new = cur + s[idx]

            res = solve(s[idx], idx + 1)
            if cur and cur + s[idx] in valid_c:
                res += solve("", idx + 1)
            return res
        
        return solve("", 0)