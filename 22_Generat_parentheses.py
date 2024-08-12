class Solution:
    def backtraking(self, n, result, left, right, str):
        if right > left:
            return 
        if left == right == n:
            result.append(str)
            return
        if left < n:
            self.backtraking(n,result,left+1,right, str + '(')
        if right < left:
            self.backtraking(n,result,left,right+1, str + ')')

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtraking(n, result, 0, 0, '') 
        return result