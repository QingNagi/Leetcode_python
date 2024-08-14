class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        else:
            if log(n, 4)%1 == 0:
                return True
            else:
                return False