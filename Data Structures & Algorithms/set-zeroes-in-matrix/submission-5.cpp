class Solution {
public:
    bool rootRow = false;
    bool rootCol = false;

    void setZeroes(vector<vector<int>>& matrix) {
        const int m = matrix.size();
        const int n = matrix.at(0).size();

        if (matrix[0][0] == 0) {
            rootRow = true;
            rootCol = true;
        }

        for (int i = 0; i < m; ++ i) {
            for (int j = 0; j < n; ++ j) {
                if (matrix[i][j] == 0) {
                    markRow(matrix, i);
                    markColumn(matrix, j);
                }
            }
        }

        for (int i = 1; i < n; ++ i) {
            if (matrix[0][i] == 0) whiteoutRow(matrix, i, m);
        }

        for (int i = 1; i < m; ++ i) {
            if (matrix[i][0] == 0) whiteoutColumn(matrix, i, n);
        }

        if (rootCol) whiteoutRow(matrix, 0, m);
        if (rootRow) whiteoutColumn(matrix, 0, n);
    }

    void markRow(vector<vector<int>>& matrix, int x) {
        if (x == 0) rootRow = true;
        else matrix[x][0] = 0;
    }

    void markColumn(vector<vector<int>>& matrix, int y) {
        if (y == 0) rootCol = true;
        else matrix[0][y] = 0;
    }

    void whiteoutColumn(vector<vector<int>>& matrix, int x, const int n) {
        for (int i = 0; i < n; ++ i) {
            matrix[x][i] = 0;
        }
    }

    void whiteoutRow(vector<vector<int>>& matrix, int y, const int m) {
        for (int i = 0; i < m; ++ i) {
            matrix[i][y] = 0;
        }
    }
};
