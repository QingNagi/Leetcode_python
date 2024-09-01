class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        memo_row = set()
        memo_col = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    memo_col.add(j)
                    memo_row.add(i)
        for i in range(row):
            for j in range(col):
                if i in memo_row or j in memo_col:
                    matrix[i][j] = 0
