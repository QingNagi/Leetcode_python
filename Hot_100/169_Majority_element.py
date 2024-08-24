class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        half = len(nums) // 2
        return nums[half]