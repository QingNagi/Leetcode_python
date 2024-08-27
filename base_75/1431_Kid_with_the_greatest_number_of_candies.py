class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_1 = max(candies)
        dp = [False] * len(candies)
        for i, y in enumerate(candies):
            if y == max_1: dp[i] = True
            if y + extraCandies >= max_1: dp[i] = True
        return dp