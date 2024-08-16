class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_dp = nums[0]
        dp = nums[0]
        for i in range(1, len(nums)):
            sum_dp = max(sum_dp+nums[i], nums[i])
            if dp < sum_dp:
                dp = sum_dp
        return dp