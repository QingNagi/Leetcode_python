class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        memo = Counter(magazine)
        for i in ransomNote:
            if i in memo: 
                memo[i] -= 1
                if memo[i] == 0:
                    del memo[i]
            elif i not in memo: return False
        return True
            