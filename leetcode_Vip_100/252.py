class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals_s =  sorted(intervals)
        for i in range(len(intervals) - 1):
            if intervals_s[i][1] > intervals_s[i+1][0]: return False
        return True