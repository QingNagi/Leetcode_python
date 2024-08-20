from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == None or len(grid) == 0:
            return 0
        result = 0
        row = len(grid)
        col = len(grid[0])
        q = deque()
        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == '1':
                    result += 1
                    q.append([i, j])
                    grid[i][j] = '0'
                while (len(q) > 0):
                    cur = q.popleft()
                    x = cur[0]
                    y = cur[1]
                    if x-1 >= 0 and grid[x-1][y] == '1':
                        grid[x-1][y] = '0'
                        q.append([x-1, y])
                    if y-1 >= 0 and grid[x][y-1] == '1':
                        grid[x][y-1] = '0'
                        q.append([x, y-1])
                    if x+1 < row and grid[x+1][y] == '1':
                        grid[x+1][y] = '0'
                        q.append([x+1, y])
                    if y+1 < col and grid[x][y+1] == '1':
                        grid[x][y+1] = '0'
                        q.append([x, y+1])
        return result