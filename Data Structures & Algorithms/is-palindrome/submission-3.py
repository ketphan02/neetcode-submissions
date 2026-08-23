class Solution:
    def is_alphanumberic(self, c: str):
        if "0" <= c <= "9":
            return c
        if "a" <= c <= "z":
            return c
        return ""

    def isPalindrome(self, s: str) -> bool:
        s = ''.join(map(self.is_alphanumberic, s.lower()))
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True