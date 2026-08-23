from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def helper(_s: str, cur: str) -> bool:
            if _s == "":
                return cur == ""
            if _s == cur:
                return cur in wordDict
            if cur in wordDict:
                return helper(_s[len(cur):], "") or helper(_s, cur + _s[len(cur)])
            return helper(_s, cur + _s[len(cur)])
        
        return helper(s, "")