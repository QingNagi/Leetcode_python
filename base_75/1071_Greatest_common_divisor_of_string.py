class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a: int, b: int) -> int:
            return a if b == 0 else gcd(b, a % b)
        if str1 + str2 != str2 + str1: return ""
        return str1[0:gcd(len(str1), len(str2))]   