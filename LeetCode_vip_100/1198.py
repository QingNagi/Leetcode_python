class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        res = -1
        if len(mat) == 1: return min(mat[0])
        memo = Counter(mat[0])
        for i in range(1, len(mat)):
            for j in list(memo.keys()):
                if j not in mat[i]: 
                    del memo[j]
                    if len(memo) == 0: return -1
        return min(list(memo.keys()))