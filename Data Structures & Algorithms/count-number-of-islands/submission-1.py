class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = 0

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            
            if visited[x][y]:
                return

            if grid[x][y] == '0':
                return
            
            visited[x][y] = True

            for dx, dy in ((0,-1),(0,1),(1,0),(-1,0)):
                dfs(x + dx, y + dy)
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    res += 1
                    dfs(i,j)

        return res