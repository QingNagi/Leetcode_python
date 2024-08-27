class Solution:
    def intToRoman(self, num: int) -> str:
        memo = dict()
        res = ''
        memo['I'] = 1
        memo['V'] = 5
        memo['X'] = 10
        memo['L'] = 50
        memo['C'] = 100
        memo['D'] = 500
        memo['M'] = 1000
        i = 0
        roman = 0
        while num > 0:
            temp = num % 10
            num = num // 10
            roman += 1
            print(roman)
            if roman == 1 and temp > 0:
                if temp == 4: res = 'IV' + res
                elif temp == 9: res = 'IX'+ res
                elif temp < 4: res = 'I' * temp + res
                elif temp >= 5: res = 'V' + 'I' * (temp - 5) + res
            if roman == 2 and temp > 0:
                if temp == 4: res = 'XL' + res
                elif temp == 9: res = 'XC' + res
                elif temp < 4: res = 'X' * temp + res
                elif temp >= 5: res = 'L' + 'X' * (temp - 5) + res
            if roman == 3 and temp > 0:
                if temp == 4: res = 'CD' + res
                elif temp == 9: res = 'CM' + res
                elif temp < 4: res = 'C' * temp  + res
                elif temp >= 5: res = 'D' + 'C' * (temp - 5) + res
            if roman >= 4 and temp > 0: res = 'M' * temp + res
        return res