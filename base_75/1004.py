class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, res, temp = 0, 0, 0
        res_max = 0 
        for j, y in enumerate(nums):
            if y == 0: temp += 1
            while temp > k:
                if nums[i] == 0 : temp -= 1
                i += 1
            res_max = max(res_max, j - i + 1)
        return res_max