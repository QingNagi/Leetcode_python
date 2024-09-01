class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_t = list(zip(*board))
        for i in range(9):
            res, res_t = 0, 0
            for j in range(9):
                if i % 3 == 0 and j % 3 == 0:
                    res_list = []
                    for i_2 in range(3):
                        for j_2 in range(3):
                            if board[i + i_2][j + j_2] != '.':
                                res_list.append(board[i + i_2][j + j_2])
                    if len(res_list) != len(set(res_list)): return False
                if board[i][j] != '.': 
                    res += 1
                if board_t[i][j] != '.':
                    res_t += 1
            if len(set(board[i])) != res+1 or len(set(board_t[i])) != res_t+1:  return False
        return True