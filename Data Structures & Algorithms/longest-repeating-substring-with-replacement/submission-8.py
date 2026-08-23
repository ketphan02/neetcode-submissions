class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        l = 0
        res = 0
        max_f = 0
        for r in range(len(s)):
            c = s[r]
            cnt[c] += 1
            max_f = max(max_f, cnt[c])
            while (r - l + 1) - max_f > k:
                cnt[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res