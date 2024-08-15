class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        memo = 1
        res = 0
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                memo += 1
            elif nums[i-1] == nums[i]:
                continue
            else:
                res = max(memo, res)
                memo = 1
        res = max(memo, res)    
        return res