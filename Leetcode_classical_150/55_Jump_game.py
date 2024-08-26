class Solution:
    def canJump(self, nums) :
        if len(nums) == 1: return True
        res, temp_max, n = 0, 0, len(nums) - 1
        end = 0
        for i,y in enumerate(nums):
            if i == n: return False
            temp_max = max(temp_max, i+y)
            if temp_max >= n:
                return True
            if i == end:
                if temp_max == end:
                    return False 
                end = temp_max
                temp_max = 0
        else: return False