class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, prev, cnt = 0, 0, 0
        for num in nums:
            cnt += 1
            if num == 0:
                prev = cnt
                cnt = 0
            res = max(res, prev + cnt)
        return res