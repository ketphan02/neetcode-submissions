from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            k = ''.join(sorted(s))
            m[k].append(s)
        
        return list(m.values())

