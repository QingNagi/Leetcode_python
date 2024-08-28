class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res, i, temp = inf, 0, 0
        for j, y in enumerate(nums):
            temp += y
            while temp >= target:
                res = min(res, j - i + 1)
                temp -= nums[i]
                i += 1
        return res if res != inf else 0