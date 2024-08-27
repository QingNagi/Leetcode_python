class Solution:
    def romanToInt(self, s: str) -> int:
        memo = dict()
        res = 0
        memo['I'] = 1
        memo['V'] = 5
        memo['X'] = 10
        memo['L'] = 50
        memo['C'] = 100
        memo['D'] = 500
        memo['M'] = 1000
        i = 0
        while i < len(s):
            if s[i] == 'I' and i < len(s) - 1 and s[i+1] in ('V', 'X'):
                if s[i+1] =='V': 
                    res += 4 
                    i += 1 
                elif s[i+1] =='X': 
                    res += 9 
                    i += 1 
                else : res += 1
            elif s[i] == 'X' and i < len(s) - 1 and s[i+1] in ('L', 'C'):
                if s[i+1] =='L': 
                    res += 40 
                    i += 1 
                elif s[i+1] =='C': 
                    res += 90 
                    i += 1 
            elif s[i] == 'C' and i < len(s) - 1 and s[i+1] in ('D', 'M'):
                if s[i+1] =='D': 
                    res += 400 
                    i += 1 
                elif s[i+1] =='M': 
                    res += 900 
                    i += 1 
            else: 
                res += memo[s[i]]
            i += 1
        return res