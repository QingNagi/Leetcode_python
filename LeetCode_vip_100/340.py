class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res, memo, i, j = 0, dict(), 0, 0
        while j < len(s):
            memo[s[j]] = memo.get(s[j], 0) + 1
            if len(memo) <= k: res = max(res, j - i + 1)
            while len(memo) > k:
                memo[s[i]] = memo.get(s[i], 0) - 1
                if memo[s[i]] == 0: del memo[s[i]]
                i += 1
            j += 1
        return res