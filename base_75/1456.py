class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        res_max = 0
        for j, y in enumerate(s):
            if y in 'aeiou': res += 1
            if j + 1 < k: continue
            res_max = max(res, res_max)
            if s[j - k + 1] in 'aeiou': res -= 1
        return res_max