class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = dict()
        for i in range(len(nums)):
            if target - nums[i] in memo:
                return [memo[target - nums[i]], i]
            else:
                memo[nums[i]] = i