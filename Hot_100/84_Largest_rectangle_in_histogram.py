class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n  # 防止 r = l
        st = []
        for i, x in enumerate(heights):
            while st and x <= heights[st[-1]]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
        right = [n] * n
        st.clear()
        for i in range(n - 1, -1, -1):
            x = heights[i]
            while st and x <= heights[st[-1]]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        ans = 0
        for h, l, r in zip(heights, left, right):
            ans = max(ans, h * (r - l - 1))
        return ans