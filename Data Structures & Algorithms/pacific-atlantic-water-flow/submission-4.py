class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        a = [[False for _ in range(n)] for _ in range(m)]
        p = [[False for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]


        def dfs(x, y, a):
            a[x][y] = True

            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                u, v = x + dx, y + dy

                if u < 0 or u >= m or v < 0 or v >= n:
                    continue
                
                if heights[x][y] > heights[u][v]:
                    continue
                
                if a[u][v]:
                    continue

                dfs(u, v, a)
        

        for i in range(n):
            dfs(0, i, a)
            dfs(m - 1, i, p)
        
        for i in range(m):
            dfs(i, 0, a)
            dfs(i, n - 1, p)
        
        res = []
        for i in range(m):
            for j in range(n):
                if a[i][j] and p[i][j]:
                    res.append([i,j])
        return res
