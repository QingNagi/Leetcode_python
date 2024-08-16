class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dict_n = Counter(nums)
        for i in nums:
            if dict_n[i] == 1:
                return i