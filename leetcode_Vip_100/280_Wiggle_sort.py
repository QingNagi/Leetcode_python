class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            if i % 2 != 0:
                if nums[i-1] <= nums[i]: continue
                else: nums[i-1], nums[i] = nums[i], nums[i-1]
            else: 
                if nums[i-1] >= nums[i]: continue
                else: nums[i-1], nums[i] = nums[i], nums[i-1]