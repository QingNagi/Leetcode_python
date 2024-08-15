class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            res = max((r - l) * min(height[r], height[l]), res)
            if height[r] > height[l]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res