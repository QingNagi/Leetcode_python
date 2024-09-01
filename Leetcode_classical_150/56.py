class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n < 2:
            return intervals
        res, i, temp, j = [], 0, 0, 0
        intervals.sort()
        while i < n - 1:
            temp = intervals[i][1]
            j = i
            while i < n - 1 and temp >= intervals[i+1][0]:
                temp = max(temp, intervals[i+1][1])
                i += 1
            res.append([intervals[j][0], temp])
            i += 1
            if i == n-1: res.append(intervals[-1])
        return res