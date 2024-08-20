class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        memo = dict()
        res = []
        for i in range(5):
            memo[i+2] = [ chr(97+3*i ), chr(98+3*i), chr(99+3*i)]
        memo[7] = [chr(97+3*5 ), chr(98+3*5), chr(99+3*5), chr(100+3*5)]
        memo[8] = [chr(101+3*5 ), chr(102+3*5), chr(103+3*5)]
        memo[9] = [chr(104+3*5), chr(105+3*5), chr(106+3*5), chr(107+3*5)]
        n = len(digits) 
        def backtrack(conbination,nextdigit, n):
            if len(conbination) == n:
                res.append(conbination)
                return
            for letter in memo[int(nextdigit[0])]:
                backtrack(conbination + letter,nextdigit[1:], n)
        res = []
        backtrack('',digits, n)
        return res