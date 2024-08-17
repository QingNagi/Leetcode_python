class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix[0]) - 1
        for i in range(len(matrix)):
            if matrix[i][len(matrix[0]) - 1] < target:
                continue
            else:
                l = 0
                while l <= r:
                    mid = l + (r - l) // 2
                    if matrix[i][mid] == target:
                        return True
                    if matrix[i][mid] > target:
                        r = mid - 1
                        if r < 0:
                            return False
                    if matrix[i][mid] < target:
                        l = mid + 1
        return False