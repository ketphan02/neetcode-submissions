class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False

        if self.size[a] > self.size[b]:
            self.parents[b] = a
            self.size[a] += self.size[b]
        else:
            self.parents[a] = b
            self.size[b] += self.size[a]
        return True

    def find(self, a):
        if a == self.parents[a]:
            return a
        
        p = self.find(self.parents[a])
        self.parents[a] = p
        return p

    def is_all_connected(self):
        return len(set([self.find(a) for a in range(len(self.parents))])) == 1

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        

        return dsu.is_all_connected()