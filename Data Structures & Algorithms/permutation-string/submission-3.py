class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1
        
        s2_count = {} # window
        start = 0
        end = 0
        while end < len(s1) - 1:
            s2_count[s2[end]] = s2_count.get(s2[end], 0) + 1
            end += 1
        
        while end < len(s2):
            s2_count[s2[end]] = s2_count.get(s2[end], 0) + 1
            if start > 0:
                s2_count[s2[start - 1]] -= 1
                if s2_count[s2[start - 1]] == 0:
                    del s2_count[s2[start - 1]]

            end += 1
            start += 1
            
            if s1_count == s2_count:
                return True

        return False



