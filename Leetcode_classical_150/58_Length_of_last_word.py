class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1: return 1 if s[-1] != ' ' else 0
        res = 0
        temp = 0
        for i, y in enumerate(s):
            if y == ' ':
                if s[i-1] != ' ' and i > 0:
                    res = i - temp
                temp = i + 1
        return len(s) - temp if s[-1] != ' ' else res