class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = 0
        state = [[1 for _ in range(n)] for _ in range(m)]

        def dfs(x, y):
            nonlocal res
            visited[x][y] = True

            for dx, dy in ((0,1),(1,0),(0,-1),(-1,0)):
                u, v = x + dx, y + dy
                if u < 0 or u >= m or v < 0 or v >= n:
                    continue
                if matrix[u][v] <= matrix[x][y]:
                    continue
                if state[u][v] > 1:
                    state[x][y] = max(state[x][y], state[u][v] + 1)
                    continue

                dfs(u, v)
                state[x][y] = max(state[x][y], state[u][v] + 1)

            res = max(res, state[x][y])
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    dfs(i, j)
        print(state)
        return res 