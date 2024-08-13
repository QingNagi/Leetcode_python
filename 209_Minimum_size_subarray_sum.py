class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        res = len(nums) + 1
        total = 0
        i, j = 0, 0
        while j < len(nums):
            total += nums[j]
            j += 1
            while total >= target:
                res = min(res, j - i)
                total -= nums[i]
                i += 1
        return 0 if res == len(nums) + 1 else res