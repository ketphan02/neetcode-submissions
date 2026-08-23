class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [idx for idx in range(n)]
        sz = [1 for _ in range(n)]
        def find(a):
            if a != parents[a]:
                parents[a] = find(parents[a])
            return parents[a]
        
        def union(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return False
            
            if sz[a] >= sz[b]:
                parents[b] = a
                sz[a] += sz[b]
            else:
                parents[a] = b
                sz[b] += sz[a]
            return True
        
        for a, b in edges:
            if union(a,b):
                n -= 1
        return n
            
        