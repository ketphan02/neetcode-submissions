from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        max_f = 0
        record = defaultdict(int)
        for r in range(len(s)):
            c = s[r]
            record[c] += 1
            max_f = max(max_f, record[c])

            while (r - l + 1) - max_f > k:
                record[s[l]] -= 1
                l += 1
        
            res = max(res, r - l + 1)
        return res