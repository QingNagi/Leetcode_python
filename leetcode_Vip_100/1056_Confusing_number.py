class Solution:
    def confusingNumber(self, n: int) -> bool:
        if n == 0 or n==1 or n==8: return False
        res, i = 0, 0
        num = int(math.log(n, 10))
        temp_n = n

        while temp_n > 0:
            temp = temp_n % 10
            temp_n = temp_n // 10
            if temp == 0 or temp == 1 or temp == 8:
                temp_res = temp
            elif temp == 6:
                temp_res = 9
            elif temp == 9:
                temp_res = 6
            else:
                break
            res = res + temp_res * pow(10, num - i)
            i += 1
        else:
            return True if res != n else False
        return False