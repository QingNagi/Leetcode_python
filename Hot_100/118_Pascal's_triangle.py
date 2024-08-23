class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        for i in range(1, numRows+1):
            dp.append([1]*i)
        if numRows < 3: return dp
        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp