class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find_set(self, v):
        if v == self.parents[v]:
            return v
        p = self.find_set(self.parents[v])
        self.parents[v] = p
        return p
    
    def union_set(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parents[b] = a
        self.size[a] += self.size[b]
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)
        num_node = n
        for edge in edges:
            a, b = edge
            if not dsu.union_set(a, b):
                return False
            num_node -= 1
        return num_node == 1