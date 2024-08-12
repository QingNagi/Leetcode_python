class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        index = 0
        for interval in intervals:
            if interval[0] < newInterval[0]:
                res.append(interval)
                index += 1
            else:
                break

        if len(res) == 0 or res[-1][1] < newInterval[0]:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1], newInterval[1])
        for i in range(index, len(intervals)):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        return res