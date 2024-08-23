class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        temp = []
        if len(prices) <= 1:
            return 0
        for i in range(len(prices)-1, -1, -1):
            if len(temp) == 0: temp.append(prices[i])
            if temp[0] < prices[i]: 
                temp.pop()
                temp.append(prices[i])
            else:
                res = max(res, temp[0] - prices[i])
        return res