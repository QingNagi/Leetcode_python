class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        temp_n, temp, i, n, min_n = 1, 0, 0, len(nums), -inf
        res = 1
        while i < n:
            if nums[i] < 0:
                temp_n *= nums[i]
                temp += 1
                min_n = max(nums[i], min_n)
            elif nums[i] > 0:
                res *= nums[i]
            i += 1
        if temp % 2 == 0 and temp > 1:
            res *= temp_n
        elif temp % 2 != 0 and temp > 1: 
            temp_n //= min_n
            res *= temp_n
        elif temp <= 1 and max(nums) <= 0:
            return max(nums)
        return res