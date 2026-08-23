from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l, r = 0, 0
        t_hsh = Counter(t)
        s_hsh = defaultdict(int)
        required = len(t_hsh)
        formed = 0

        while r < len(s):
            c = s[r]
            s_hsh[c] += 1
            if c in t_hsh and s_hsh[c] == t_hsh[c]:
                formed += 1

            while l <= r and formed == required:
                c = s[l]
                if not res or len(res) > r - l + 1:
                    res = s[l:r+1]
                
                s_hsh[c] -= 1
                if c in t_hsh and s_hsh[c] < t_hsh[c]:
                    formed -= 1
                l += 1

            r += 1
            
        return res