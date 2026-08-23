class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        res = 0
        store = set()
        for c in s:
            if c not in store:
                store.add(c)
            else:
                while True:
                    if s[i] == c:
                        i += 1
                        break
                    store.remove(s[i])
                    i += 1
            res = max(res, len(store))
        return res