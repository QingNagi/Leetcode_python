class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre_max = pre_min = ans = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            ans = max(ans, cur_max)
            pre_max, pre_min = cur_max, cur_min
        return ans