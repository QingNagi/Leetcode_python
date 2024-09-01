class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:   return [newInterval]
        res = []
        i, n = 0, len(intervals)
        if newInterval[1] < intervals[0][0]: 
            res.append(newInterval)
        while i < n:
            if 0 < i and newInterval[0] > intervals[i-1][1] and newInterval[1] < intervals[i][0]:
                res.append(newInterval)
            if newInterval[0] > intervals[i][1]: 
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]: 
                res.append(intervals[i])
            else:
                temp = min(intervals[i][0], newInterval[0])
                temp_max = max(intervals[i][1], newInterval[1])
                while i < n and temp_max >= intervals[i][0]:
                    temp_max = max(intervals[i][1], temp_max)
                    i += 1
                res.append([temp, temp_max])
                i -= 1
            i += 1
        if newInterval[0] > intervals[-1][1]: 
            res.append(newInterval)
        return res