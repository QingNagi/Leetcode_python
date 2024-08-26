class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1
        res = len(nums)
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]: 
                nums[i-1] = inf
                res -= 1
        nums.sort()
        return res