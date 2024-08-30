class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n, m = len(nums), len(str(nums[0]))
        ans = m * n * (n - 1) // 2
        cnt = [[0] * 10 for _ in range(m)]
        for x in nums:
            i = 0
            while x:
                x, d = divmod(x, 10)
                ans -= cnt[i][d]
                cnt[i][d] += 1
                i += 1
        return ans