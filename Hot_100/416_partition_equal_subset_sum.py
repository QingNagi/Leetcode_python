class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2: return False
        all_sum = sum(nums)
        if  all_sum % 2 != 0: return False
        target = all_sum // 2
        f = [True] + [False] * target
        s2 = 0
        for i,x in enumerate(nums):
            s2 = min(s2+x, target)
            for j in range(s2, x-1, -1):
                f[j] = f[j] or f[j -x]
        return f[target]