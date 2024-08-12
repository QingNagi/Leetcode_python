class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        self.dfs(nums, res, 0, [])
        return res

    def dfs(self, nums, res, index, subset):
        res.append(subset.copy())
        if index == len(nums):
            return
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, res, i+1, subset)
            subset.pop()