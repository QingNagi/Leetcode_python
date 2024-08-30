class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        memo = Counter(s)
        memo_2 = Counter(t)
        for i in s:
            if memo[i] != memo_2[i]: return False
        return True