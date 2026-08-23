class Solution {
public:
    const vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    int curDir = 0;
    vector<vector<bool>> visited;
    vector<int> res;

    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        const int m = matrix.size(); // num rows;
        const int n = matrix.at(0).size(); // num columns;
        visited = vector(m, vector(n, false));
        dfs(matrix, 0, 0, m, n, 0);
        return res;
    }

    void dfs(vector<vector<int>>& matrix, int x, int y, const int m, const int n, int cnt) {
        if (cnt >= 2) {
            return;
        }

        if (cnt == 0) {
            res.push_back(matrix[x][y]);
            visited[x][y] = true;
        }
        
        int u = x + directions[curDir].first;
        int v = y + directions[curDir].second;
        if (u < 0 || u >= m || v < 0 || v >= n || visited[u][v]) {
            curDir = (curDir + 1) % 4;
            dfs(matrix, x, y, m, n, cnt + 1);
        } else {
            dfs(matrix, u, v, m, n, 0);
        }
    }
};
