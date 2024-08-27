class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        i, j = 0, n-1
        s2 = list(s)
        while i < j:
            while i < j and s[j] not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'): j -= 1
                        
            while i < j and s[i] not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'): i += 1
            s2[i], s2[j] = s2[j], s2[i]
            i += 1
            j -= 1
        return ''.join(s2)