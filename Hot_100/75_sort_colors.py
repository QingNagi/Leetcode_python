class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j= 0, len(nums)-1
        while i < j:
            while nums[i] == 0 and i < j:
                i += 1
            while nums[j] != 0 and j > i:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        j= len(nums)-1
        while i < j:
            while nums[i] == 1 and i < j:
                i += 1
            while nums[j] != 1 and j > i:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]