class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        if n == 1: 
            for j in range(m-1):
                if grid[0][j] == grid[0][j+1]:  return False
            return True
        elif m == 1:
            for i in range(n-1):
                if grid[i+1][0] != grid[i][0]:  return False
            return True
        if n<=1 and m<=1: return True
        for i in range(n-1):
            for j in range(m-1):
                if grid[i][j] == grid[i][j+1] or grid[i+1][j] != grid[i][j]: 
                    return False
        return True if grid[-1][-1] == grid[-2][-1] else False