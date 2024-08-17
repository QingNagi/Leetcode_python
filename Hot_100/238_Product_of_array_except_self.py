class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, tmp = [1] * len(nums), 1
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1] # 下三角
            print(ans)
        for i in range(len(nums) - 2, -1, -1):
            tmp *= nums[i + 1]                # 上三角
            print(tmp)
            ans[i] *= tmp                     # 下三角 * 上三角
        return ans