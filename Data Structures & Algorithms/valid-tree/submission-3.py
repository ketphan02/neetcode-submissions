class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = [idx for idx in range(n)]
        rank = [1 for _ in range(n)]

        def find(a):
            p = parents[a]
            if a == p:
                return a
            root = find(p)
            parents[p] = root
            return root
        
        def merge(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return False
            if rank[a] > rank[b]:
                parents[b] = a
            elif rank[b] > rank[a]:
                parents[a] = b
            else:
                parents[b] = a
                rank[a] += 1
            return True
        
        for a, b in edges:
            if not merge(a, b):
                return False
            n -= 1
        return n == 1
            