class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        track = set()
        for c in s:
            if c not in track:
                track.add(c)
            else:
                while c in track:
                    track.remove(s[l])
                    l += 1
                track.add(c)
            res = max(res, len(track))

        return res