class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, cur, res):
        res.append(cur)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                self.dfs(nums[i+1:], cur + [nums[i]], res)
