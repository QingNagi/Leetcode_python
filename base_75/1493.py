class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i , res_max, temp = 0, 0, 0
        for j,y in enumerate(nums):
            if y == 0: temp += 1
            res_max = max(res_max, j - i + 1 - temp)
            while temp > 1: 
                if nums[i] == 0: temp -= 1
                i += 1
        return res_max if temp != 0 else res_max - 1