class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, res, [])
        return res

    def backtrack(self, nums, res, list1):
        if len(nums) == len(list1):
            res.append(list1.copy())
            return

        for num in nums:
            if num not in list1:
                list1.append(num)
                self.backtrack(nums, res, list1)
                list1.pop()