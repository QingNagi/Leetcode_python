class Solution:
    def findMaxAverage(self, nums, k):
        i = 0
        total = sum(nums[:k])
        tmp = sum(nums[:k])
        for num in nums[k:]:
            tmp = tmp - nums[i] + num
            total = max(total, tmp)
            i += 1
        return total / k