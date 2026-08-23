class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0

        def dfs(i, j):
            nonlocal visited, res
            visited[i][j] = True

            for direction in directions:
                u = i + direction[0]
                v = j + direction[1]
                
                if u < 0 or u >= m or v < 0 or v >= n:
                    res += 1
                    continue
            
                if visited[u][v]:
                    continue
                
                if grid[u][v] != 1:
                    res += 1
                    continue
                
                dfs(u, v)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return res
