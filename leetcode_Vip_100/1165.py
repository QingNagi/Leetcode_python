class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        j, res, memo = 0, 0, defaultdict()
        for i, y in enumerate(keyboard):
            memo[y] = i
        for i in word:
            res += abs(memo[i] - j)
            j = memo[i]
        return res