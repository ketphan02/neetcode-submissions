class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]


        def _word_searcher(i: int, j: int, search_idx: int) -> bool:
            if search_idx >= len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if word[search_idx] != board[i][j]:
                return False
            if visited[i][j]:
                return False

            visited[i][j] = True

            for dx, dy in ((0,1),(1,0),(0,-1),(-1,0)):
                u, v = dx + i, dy + j
                if _word_searcher(u, v, search_idx + 1):
                    return True

            visited[i][j] = False
            return False


        for i in range(m):
            for j in range(n):
                if _word_searcher(i, j, 0):
                    return True
        
        return False