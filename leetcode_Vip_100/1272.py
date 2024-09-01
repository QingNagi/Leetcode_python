class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if intervals[i][1] >= toBeRemoved[1] and intervals[i][0] <= toBeRemoved[0]:
                if intervals[i][0] != toBeRemoved[0]:
                    res.append([intervals[i][0], min(toBeRemoved[0], intervals[i][1])])
                if intervals[i][1] != toBeRemoved[1]:
                    res.append([max(toBeRemoved[1],intervals[i][0]),intervals[i][1]])
            elif intervals[i][0] > toBeRemoved[1]: res.append(intervals[i])
            elif toBeRemoved[0] > intervals[i][0]:
                res.append([intervals[i][0], min(toBeRemoved[0], intervals[i][1])])
            elif toBeRemoved[0] < intervals[i][0] and toBeRemoved[1] < intervals[i][1]:
                res.append([toBeRemoved[1], intervals[i][1]])
        return res