class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        memo = defaultdict(str)
        s += ' '
        j, temp, n = 0, '', len(pattern) - 1
        for i in s:
            if i != ' ':
                temp += i
            elif i == ' ':
                if j > n: return False
                if temp not in memo and pattern[j] not in memo.values():
                    memo[temp] = pattern[j]
                    j +=1
                elif memo[temp] == pattern[j]: 
                    j += 1
                elif memo[temp] != pattern[j] or memo[pattern[j]] != temp: return False
                temp = ''
        if j < n+1: return False
        return True