class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(x, y):
            board[x][y] = 'P'

            for direction in directions:
                u = x + direction[0]
                v = y + direction[1]

                if 0 <= u and u < m and 0 <= v and v < n and board[u][v] == "O":
                    dfs(u, v)
        
        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][-1] == "O":
                dfs(i, n - 1)
        for i in range(n):
            if board[0][i] == "O":
                dfs(0, i)
            if board[-1][i] == "O":
                dfs(m - 1, i)
        
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "P":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
                    