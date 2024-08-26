class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 2: return 2
        res = len(nums)
        for i in range(2, len(nums)):
            if nums[i-1] == nums[i] and nums[i-2] == nums[i-1]:
                nums[i-2] = inf
                res -= 1
        nums.sort()
        return res