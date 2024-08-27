class Solution:
    def reverseWords(self, s: str) -> str:
        def revers(s):
            i, j = 0, len(s) -1
            while i < j:
                s[i], s[j] = s[j], s[i]
        res, temp = '', ''
        for i, y in enumerate(s):
            if y != ' ':
                temp += y
            else: 
                if temp != '':
                    res = ' ' + temp + res
                temp =''
        if s[-1] != ' ':
            res = temp + res
        else: s= s[:-1]
        return res if res[0] != ' ' else res[1:]