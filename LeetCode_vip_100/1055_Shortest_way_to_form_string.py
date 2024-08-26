class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s, res = 0, 0
        while s < len(target):
            i = 0
            temp = s
            for i in range(len(source)):
                if source[i] == target[s]: s += 1
                if s == len(target): break
            if temp == s: break
            res += 1
        else: 
            return res
        return -1