class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, memo, res = 0, dict(), 0
        for j, y in enumerate(s):
            memo[y] = memo.get(y, 0) + 1
            while memo[y] > 1:
                memo[s[i]] = memo[s[i]] - 1
                if memo[s[i]] == 0: del memo[s[i]]
                i += 1
            res = max(res, j-i+1)
        return res