class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if nums == None or len(nums) == 0:
            return 0
        while l < r:
            mid = l + (r - l) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l if nums[l] >= target else l + 1