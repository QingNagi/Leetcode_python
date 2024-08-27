class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = list()
        if numRows == 1: return s
        while len(res) < numRows:
            res.append('')
        i = 0
        stat = 0
        temp = 0
        for y in s:
            if stat == 0 :
                res[temp] += y
                temp += 1
                if temp == numRows:
                    stat = 1
                    temp -= 1
            elif stat == 1: 
                temp -= 1
                res[temp] += y
                if temp == 0:
                    stat = 0
                    temp += 1
        res_s = ''
        for i in range(len(res)):
            res_s += res[i] 
        return res_s