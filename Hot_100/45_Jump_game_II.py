class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        max_i, end = 0, 0
        if len(nums) < 2:
            return 0
        for i in range(len(nums)):
            if max_i >= i and max_i < i + nums[i]:
                max_i = i + nums[i]
            if max_i >= len(nums) - 1:
                return step + 1
            if i == end:
                end = max_i
                step += 1