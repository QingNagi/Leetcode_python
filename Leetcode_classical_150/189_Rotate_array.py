class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        while k > n:
            k -= n
        nums[:k], nums[k:] = nums[n-k:], nums[:n-k]