class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        temp = 0
        l = -1
        if len(s) < 1:
            return 0
        memo = dict()
        for i in range(len(s)):
            if (s[i] in memo) and (l < memo[s[i]]):
                l = memo[s[i]] 
                memo[s[i]] = i
            else:
                memo[s[i]] = i
                temp = i - l 
                res = max(res, temp)
        res = max(res, temp)
        return res