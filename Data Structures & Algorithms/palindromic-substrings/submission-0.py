class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        def get_pal(l, r):
            nonlocal res
            if l < 0 or r >= len(s):
                return

            if s[l] != s[r]:
                return
            
            res += 1
            get_pal(l - 1, r + 1)
        
        for idx in range(len(s)):
            get_pal(idx, idx)
            print()
            get_pal(idx, idx + 1)
        
        return res
            