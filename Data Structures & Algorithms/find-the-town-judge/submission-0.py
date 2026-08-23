from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(set)
        trusting = [0 for _ in range(n + 1)]

        for t in trust:
            a, b = t
            trusted[b].add(a)
            trusting[a] += 1

        judge=-1
        for p in trusted.keys():
            if len(trusted[p]) == n - 1 and trusting[p] == 0:
                if judge != -1:
                    return -1
                judge = p

        return judge