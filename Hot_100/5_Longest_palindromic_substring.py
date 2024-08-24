class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_search_longest(left: int, right: int):
            n = len(s)
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        n = len(s)
        length = 1 
        start = 0  
        for i in range(n):
            odd_len = expand_search_longest(i, i)       
            even_len = expand_search_longest(i, i+1)   
            local_max = max(odd_len, even_len)   
            if local_max > length:
                length = local_max
                start = i - (local_max - 1) // 2    
        return s[start: start + length] 