class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if self.size[a] > self.size[b]:
            self.parents[b] = a
            self.size[a] += self.size[b]
        else:
            self.parents[a] = b
            self.size[b] += self.size[a]

    def find(self, a):
        if a == self.parents[a]:
            return a
        
        p = self.find(self.parents[a])
        self.parents[a] = p
        return p
    
    def unique_components(self):
        return len({ self.find(i) for i in range(len(self.parents)) })

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)
        
        return dsu.unique_components()
        
