class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        total = sum(nums)
        all_total = ((max(nums)+1)*max(nums))//2
        if total == all_total:
            return len(nums)
        else:
            return all_total - total