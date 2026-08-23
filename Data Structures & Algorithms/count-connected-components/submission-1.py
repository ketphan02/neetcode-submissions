
class DSU:
    def __init__(self, n):
        # Make set
        self.n = n
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find_set(self, v):
        if self.parent[v] == v:
            return v
        p = self.find_set(self.parent[v])
        self.parent[v] = p
        return p

    def union(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]

    def num_parents(self):
        s = set()
        for v in range(self.n):
            s.add(self.find_set(v))
        return len(s)

class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for edge in edges:
            dsu.union(edge[0], edge[1])
        return dsu.num_parents()
