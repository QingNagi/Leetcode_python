class Solution:
    def isArmstrong(self, n: int) -> bool:
        sum_all, res_all = [], 0
        res = n
        while res:
            res, res_div = divmod(res, 10)
            sum_all.append(res_div)
        n_res = len(sum_all)
        for i in sum_all:
            res_all += pow(i ,n_res)
        return res_all == n