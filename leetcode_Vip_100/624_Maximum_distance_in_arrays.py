class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maxValue, maxIndex = -inf, -1
        arrays.sort(key=lambda x: x[0])
        for i in range(len(arrays)):
            if arrays[i][-1] > maxValue:
                maxValue, maxIndex = arrays[i][-1], i
        else:
            if maxIndex != 0:
                return maxValue - arrays[0][0]
            else:
                candidate, minValue = maxValue - arrays[1][0], arrays[0][0]
                arrays.sort(key=lambda x: x[-1])
                return max(candidate, arrays[-2][-1] - minValue)