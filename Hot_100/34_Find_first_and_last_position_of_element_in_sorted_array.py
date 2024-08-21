class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 0:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l)>>1)
            if nums[mid] == target:
                l = mid
                break
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        if nums[l] != target:
            return [-1, -1]
        else:
            l1 = l2 = l 
            while True:
                if nums[l1] == target and l1 > 0:
                    l1 -= 1
                if nums[l2] == target and l2 < len(nums) - 1:  
                    l2 += 1
                if (nums[l2] != target or nums[-1] == target) and (nums[l1] != target or nums[0]==target):
                    if nums[0]==target:
                        l1 = -1
                    if nums[-1] == target:
                        l2 = len(nums)
                    return [l1 + 1, l2 - 1]