class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        res = ''
        n = len(s)
        shift_1, orit = 0, -1
        for i in range(len(shift)):
            if shift[i][0] == 0: shift_1 += shift[i][1]
            else : shift_1 -= shift[i][1]
            while shift_1 > n:
                shift_1 = shift_1 - n
            while shift_1 < -n:
                shift_1 = shift_1 + n
        else:
            res = ''
            if shift_1 > 0:
                res += s[shift_1:]
                res += s[:shift_1]
            elif shift_1 < 0:
                shift_1 = -shift_1
                res += s[n - shift_1:]
                res += s[:n- shift_1]
            else:
                return s
        return res