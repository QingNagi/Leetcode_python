class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        if matrix[r][-1] < target:
            return False
        if r == 0:
            row = 0
        else:
            while l < r:
                mid = l + (r - l) // 2
                if matrix[mid][-1] == target:
                    return True
                if matrix[mid][-1] > target:
                    r = mid
                else:
                    l = mid + 1
            row = l 
        print(row)
        l, r = 0, len(matrix[0]) - 1
        while l < r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                r = mid
            else:
                l = mid + 1
        return False if matrix[row][l] != target else True