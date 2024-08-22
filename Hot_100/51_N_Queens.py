class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        col = [0] * n
        def dfs(r, s):
            if r == n:
                print(col)
                ans.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in col])
                return
            for c in s:
                if all(r+c != R+col[R] and r - c != R - col[R] for R in range(r)):
                    col[r] = c
                    dfs(r+1, s-{c})
        dfs(0, set(range(n)))
        return ans