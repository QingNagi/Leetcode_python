class Solution:
    def isHappy(self, n: int) -> bool:
        fast = n
        slow = n
        while True:
            # 快慢指针异速前进
            fast = self.getNext(fast)
            fast = self.getNext(fast)
            slow = self.getNext(slow)
            if fast == 1:
                return True
            if fast == slow:
                return False
    # 取各位数字的平方和，即下一个数
    def getNext(self, num: int) -> int:
        sum = 0
        localNum = num
        while localNum > 0:
            unitsDigit = localNum % 10  # 取个位数字
            sum += unitsDigit * unitsDigit
            localNum //= 10
        return sum