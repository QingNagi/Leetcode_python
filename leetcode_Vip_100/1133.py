class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        memo = Counter(nums)
        res = -1
        for i, y in memo.items():
            if y == 1: res = max(res, i)
        return res