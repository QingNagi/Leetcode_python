class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])
        if fresh == 0:
            return time
        if len(q) <= 0:
            return -1
        while q:
            time += 1
            temp = q
            q = []
            while len(temp) > 0:
                x = temp.pop()
                for i, j in ((x[0]+1,x[1]), (x[0]-1,x[1]), (x[0],x[1]+1), (x[0],x[1]-1)):
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        fresh -= 1
                        grid[i][j] = 2
                        q.append([i,j])
        if fresh == 0: 
            return time - 1
        else: 
            return -1