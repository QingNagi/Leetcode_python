class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        index = -1
        while l < r:
            mid = l + ((r -l)>>1)
            if nums[mid] <= nums[-1] :
                r = mid
            else:
                l = mid + 1 
        rot = r - 1
        return nums[rot+1]