class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(map(lambda x: x if x.isalnum() else '', s.lower()))
        return s == s[::-1]