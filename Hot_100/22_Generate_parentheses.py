class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtraking(n, res, '', 0, 0)
        return res

    def backtraking(self, n, res, List1, r, l):
        if r > l:
            return
        if l == r == n:
            res.append(List1)
            return
        if l < n:
            self.backtraking(n, res, List1+'(', r, l+1)
        if r < n:
            self.backtraking(n, res, List1+')', r+1, l)