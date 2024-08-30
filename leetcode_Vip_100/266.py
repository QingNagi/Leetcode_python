class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        memo, temp = Counter(s), 0
        if len(s) % 2 == 0:
            for i in memo.values():
                if i % 2 != 0: return False
        if len(s) % 2 == 1:
            for i in memo.values():
                if i % 2 != 0: 
                    temp += 1
                    if temp > 1: return False
        return True