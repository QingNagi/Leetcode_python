class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.backtracking(n, k, self.res, 1, [])
        return self.res

    def backtracking(self, n, k, rs, begin, list1):
        if len(list1) == k:
            self.res.append(list1.copy())
            return

        for i in range(begin, n+1):
            list1.append(i)
            self.backtracking(n, k, self.res, i+1, list1)
            list1.pop()