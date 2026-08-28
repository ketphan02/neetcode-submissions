class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        def get_palindrome(l, r):
            nonlocal res

            if l < 0 or r >= len(s):
                return
            
            if s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r + 1]
                get_palindrome(l - 1, r + 1)
        
        for i in range(len(s)):
            get_palindrome(i, i)
            get_palindrome(i, i + 1)
        
        return res