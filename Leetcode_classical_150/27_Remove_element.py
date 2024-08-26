class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums : return 0
        i, j, res = 0, len(nums) - 1, 0
        if j == 0: 
            if nums[0] != val: return 1
            else: return 0
        while i < j:
            while nums[i] != val and i < j: 
                i += 1 
                res += 1
            while nums[j] == val and i < j: 
                nums[j] = '_'
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return res if nums[i] == val else res + 1