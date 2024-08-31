class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        flag = True
        while flag:
            flag = False
            rem = []
            # 水平
            for i in range(m):
                pre = board[i][0]
                cnt = 1
                for j in range(1, n):
                    if pre == board[i][j]:
                        cnt += 1
                    else:
                        if cnt >= 3 and pre:
                            rem.extend([i, k] for k in range(j - cnt, j))
                        cnt = 1
                        pre = board[i][j]
                if cnt >= 3 and pre:
                    rem.extend([i, k] for k in range(n - cnt, n))
            # 竖直
            for j in range(n):
                pre = board[0][j]
                cnt = 1
                for i in range(1, m):
                    if pre == board[i][j]:
                        cnt += 1
                    else:
                        if cnt >= 3 and pre:
                            rem.extend([k, j] for k in range(i - cnt, i))
                        cnt = 1
                        pre = board[i][j]
                if cnt >= 3 and pre:
                    rem.extend([k, j] for k in range(m - cnt, m))
            if rem:
                flag = True
                for i, j in rem:
                    board[i][j] = 0
                # 移动值
                for j in range(n):
                    lst = []
                    for i in range(m - 1, -1, -1):
                        if board[i][j]:
                            lst.append(board[i][j])
                        board[i][j] = 0
                    k = len(lst)
                    for i in range(m - 1, m - k - 1, -1):
                        board[i][j] = lst[m - 1 - i]
        return board