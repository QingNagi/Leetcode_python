class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        for i in range(1, len(nums)+1):
            self.backtarking(nums, res, [], i, 0)
        return res
    def backtarking(self, nums, res, list1, length, index):
        if len(list1) == length:
            res.append(list1.copy())
        for i in range(index, len(nums)):
            list1.append(nums[i])
            self.backtarking(nums, res, list1, length, i+1)
            list1.pop()
