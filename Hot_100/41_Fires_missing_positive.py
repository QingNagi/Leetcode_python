class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if nums[-1] <= 0:
            return 1
        for i in range(len(nums)):
            if nums[i] > 0:
                print(nums[i])
                if nums[i] != 1:
                    return 1
                else:
                    while i < len(nums) - 1:
                        i += 1
                        if nums[i] > nums[i-1] + 1:
                            return nums[i-1] + 1
                    return nums[i] + 1   