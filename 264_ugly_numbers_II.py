class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = dict()
        dp[1] = 1
        p2, p3, p5 = 1, 1, 1
        for i in range(2, n+1):
            t2 = dp[p2] * 2
            t3 = dp[p3] * 3
            t5 = dp[p5] * 5

            dp[i] = min(t2, t3, t5)
            if t2 == dp[i]:
                p2 += 1
            if t3 == dp[i]:
                p3 += 1
            if t5 == dp[i]:
                p5 += 1
        return dp[n]
