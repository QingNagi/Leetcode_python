class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, res, [])
        return res

    def backtrack(self, nums, res, list1):
        if len(list1) == len(nums):
            res.append(list1.copy())
        for i in range(len(nums)):
            if nums[i] in list1: continue
            list1.append(nums[i])
            self.backtrack(nums, res, list1)
            list1.pop()