class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [0] + [inf] * amount
        for i in coins:
            for j in range(i, amount+1):
                res[j] = min(res[j], res[j-i]+1)
        return res[amount] if res[amount] != inf else -1