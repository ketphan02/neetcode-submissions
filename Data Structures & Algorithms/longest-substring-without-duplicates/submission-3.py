class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, cur = 0, 0
        chars = set()
        res = 0
        for c in s:
            if c in chars:
                while s[start] != c:
                    chars.remove(s[start])
                    start += 1
                chars.remove(s[start])
                start += 1

            chars.add(c)
            res = max(res, len(chars))
        return res
        