class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        hsh = defaultdict(int)
        res = 0

        def get_most_freq_value():
            return max(hsh.values())

        while r < len(s):
            c = s[r]

            hsh[c] += 1
            w = r - l + 1
            while l < r and w - get_most_freq_value() > k:
                hsh[s[l]] -= 1
                l += 1
                w = r - l + 1
            
            res = max(res, w)
            r += 1

        return res
