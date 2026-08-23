class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = Counter(t)
        window = {}
        current_qualified, total_qualified = 0, len(t)

        l = 0
        res = ""
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1

            if c in t and window[c] == t[c]:
                current_qualified += 1
            while current_qualified == total_qualified:
                if res == "" or len(res) > r - l + 1:
                    res = s[l:r + 1]

                window[s[l]] -= 1
                if s[l] in t and window[s[l]] < t[s[l]]:
                    current_qualified -= 1
                l += 1
                
        return res