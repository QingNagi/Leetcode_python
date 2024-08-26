class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        res = 0
        end, temp_max, n = 0, 0, len(nums) - 1
        for i, y in enumerate(nums):
            temp_max = max(temp_max, (i +y))
            if temp_max >= n: return res + 1
            if end == i:
                end = temp_max
                res += 1
        return res