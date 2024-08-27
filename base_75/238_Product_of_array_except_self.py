class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            dp[i] = dp[i-1] * nums[i-1]
        dp_2 = [0] * len(nums)
        dp_2[len(nums)-1] = 1
        for j in range(len(nums)-2, -1, -1):
            dp_2[j] = dp_2[j+1] * nums[j+1] 
        for i in range(len(nums)):
            dp[i] = dp[i] * dp_2[i]
        return dp