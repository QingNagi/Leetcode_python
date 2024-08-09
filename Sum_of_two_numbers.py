class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in map:
                return [i,map[diff]]
            else:
                map[nums[i]] = i
                 