class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        i, res, memo = 0, 0, dict()
        for j in range(len(s)):
            memo[s[j]] = memo.get(s[j], 0) + 1
            if j - i + 1 > k:
                memo[s[i]] = memo.get(s[i], 0) - 1
                if memo[s[i]] == 0: del memo[s[i]]
                i += 1
            while memo[s[j]] > 1:
                memo[s[i]] = memo.get(s[i], 0) - 1
                if memo[s[i]] == 0: del memo[s[i]]
                i += 1
            if len(memo) == k: 
                res += 1
        return res