class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjlist = {c: set() for w in words for c in w}
        indegree = {c: 0 for c  in adjlist.keys()}

        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                idx = 0
                a, b = words[i], words[j]
                flag = False
                while idx < len(a) and idx < len(b):
                    if a[idx] == b[idx]:
                        idx += 1
                        continue

                    if b[idx] not in adjlist[a[idx]]:
                        adjlist[a[idx]].add(b[idx])
                        indegree[b[idx]] += 1
                    flag = True
                    break
                if not flag and len(a) > len(b):
                    return ""
        
        q = deque()
        for c in indegree.keys():
            if indegree[c] == 0:
                q.append(c)
        
        res = ''
        while q:
            c = q.popleft()
            res += c
            for nei in adjlist[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return res if len(res) == len(indegree) else ""
                    

