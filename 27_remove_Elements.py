class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        l, r = 0, len(nums) - 1
        while l < r:
            while(l < r and nums[l] != val):
                l += 1
            while(l < r and nums[r] == val):
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
        return l if nums[l] == val else l+1
