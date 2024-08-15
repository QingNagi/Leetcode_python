class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        pre_max = 0
        res = 0
        suf_max = 0
        while l < r:
            pre_max = max(pre_max, height[l])
            suf_max = max(suf_max, height[r])
            if pre_max < suf_max:
                res += pre_max - height[l]
                l += 1
            else:
                res += suf_max - height[r]
                r -= 1
        return res