class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if n < m: return -1
        i, temp,j = 0, 0, 0
        while i < n:
            if haystack[i] == needle[0]:
                temp = i
                i += 1
                j += 1
                if j == m: return temp
                while i < n and j < m:
                    if haystack[i] == needle[j]:
                        i += 1
                        j += 1
                        if j == m: return temp
                    else: 
                        j = 0 
                        i = temp + 1
                        break
            else: i += 1
        else: return -1