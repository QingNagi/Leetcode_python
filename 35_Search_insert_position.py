class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if nums == None or n == 0:
            return 0
        left = 0
        right = n - 1
        while(left < right):
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left if nums[left] >= target else left + 1