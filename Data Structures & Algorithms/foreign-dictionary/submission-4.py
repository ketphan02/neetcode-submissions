class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        wordlist = list(set(''.join(words)))
        adj = {c: set() for c in wordlist}
        indegree = {c: 0 for c in wordlist}

        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                a, b = words[i], words[j]

                idx = 0
                while idx < min(len(a), len(b)):
                    c_a, c_b = a[idx], b[idx]
                    if len(a) > len(b) and a.startswith(b):
                        return ""
                                        
                    if c_a != c_b:
                        if c_b not in adj[c_a]:
                            adj[c_a].add(c_b)
                            indegree[c_b] += 1
                        break
                    
                    idx += 1


        print(adj, indegree)

        s = [c for c in wordlist if c not in indegree or indegree[c] == 0]
        res = []
        while s:
            top = s.pop()
            res.append(top)

            for nei in adj[top]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    s.append(nei)
        
        return ''.join(res) if len(res) == len(wordlist) else ''
