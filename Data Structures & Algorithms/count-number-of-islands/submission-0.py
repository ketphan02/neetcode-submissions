class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols and not visited[x][y] and grid[x][y] == "1"

        def dfs(x, y):
            visited[x][y] = True

            for move in moves:
                u, v = x + move[0], y + move[1]
                if is_valid(u, v):
                    dfs(u, v)

        res = 0
        for i in range(rows):
            for j in range(cols):
                if is_valid(i, j):
                    dfs(i, j)
                    res += 1

        return res