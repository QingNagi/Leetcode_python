class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_1, min_1 = -1, inf
        res = 0
        max_index, min_index = 0, len(prices)
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > max_1: 
                max_1 = prices[i] 
                max_index = i
            elif prices[i] < min_1 : 
                min_1 = prices[i]
                min_index = i
            else: 
                continue
            if max_index > min_index:
                res = max(res, max_1 - min_1)
            min_1 = max_1
        return res