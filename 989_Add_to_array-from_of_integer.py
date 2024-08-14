class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        temp = 0
        num = deque(num)
        total = k
        for i in range(len(num)-1, -1, -1):
            total = num[i] + total
            num[i] = total % 10
            total //= 10
        while total > 0:
            num.appendleft(total % 10)
            total //= 10

        return list(num)