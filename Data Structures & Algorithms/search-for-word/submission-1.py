class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(i, j, cur_idx):
            nonlocal visited
            if cur_idx >= len(word):
                return True

            for direction in directions:
                u = i + direction[0]
                v = j + direction[1]

                if 0 <= u and u < m and 0 <= v and v < n and board[u][v] == word[cur_idx] and not visited[u][v]:
                    print(u, v, visited[u][v])
                    visited[u][v] = True
                    if dfs(u, v, cur_idx + 1):
                        return True
                    visited[u][v] = False
            
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if dfs(i, j, 1):
                        return True
                    visited[i][j] = False
        return False
                    