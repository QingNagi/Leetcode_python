class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        perfix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(strs[i]) and j < len(perfix):
                if strs[i][j] != perfix[j]:  
                    if j == 0: return '' 
                    perfix = perfix[:j]
                j += 1
            perfix = perfix[:j]
        return perfix