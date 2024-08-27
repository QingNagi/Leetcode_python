class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        l_max, r_max = height[l], height[r] 
        res = 0
        while l < r:
            if l_max <= r_max:
                l += 1
                if l_max < height[l]: l_max = height[l]
                else: res += l_max - height[l]
            else: 
                r -= 1
                if r_max < height[r]: r_max = height[r]
                else: res += r_max - height[r]
        return res