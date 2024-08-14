class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        temp = 0
        num = deque(num)
        for i in range(len(num)-1, -1, -1):
            remainder = k % 10
            k //= 10
            total = num[i] + remainder + temp
            print(total, k)
            temp = total // 10
            num[i] = total % 10
        
        while k != 0 or temp == 1:
            remainder = k % 10
            k //= 10
            total = remainder + temp
            print(total, k)
            temp = total // 10
            num.appendleft(total % 10)

        return list(num)