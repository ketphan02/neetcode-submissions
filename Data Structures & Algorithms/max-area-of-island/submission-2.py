class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        cnt = 0
        def dfs(x, y):
            nonlocal cnt
            grid[x][y] = 0
            cnt += 1

            for direction in directions:
                u = x + direction[0]
                v = y + direction[1]

                if 0 <= u and u < m and 0 <= v and v < n and grid[u][v] == 1:
                    dfs(u, v)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = 0
                    dfs(i, j)
                    res = max(res, cnt)
        return res