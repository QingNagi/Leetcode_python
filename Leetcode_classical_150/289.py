class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        n, m = len(board), len(board[0])
        res_1, res_0 = [], []
        for i in range(n):
            for j in range(m):
                tmep = 0
                for i_1 in range(-1, 2):
                    for j_1 in range(-1, 2):
                        if i + i_1 > n-1 or i + i_1 < 0 or j + j_1 > m-1 or j + j_1 < 0 or (i_1==0 and j_1==0): continue
                        if board[i+i_1][j+j_1] == 1:
                            tmep += 1
                        if [i+i_1, j+j_1] in res_1: tmep -= 1
                        elif [i+i_1, j+j_1] in res_0: tmep += 1
                if board[i][j] == 0:
                    if tmep == 3: 
                        board[i][j] = 1
                        res_1.append([i, j])
                elif board[i][j] == 1:
                    if tmep < 2 or tmep > 3: 
                        board[i][j] = 0
                        res_0.append([i, j])