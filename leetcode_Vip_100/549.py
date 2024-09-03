class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 1
        def dfs(root):
            if not root: return
            left, right = dfs(root.left), dfs(root.right)
            inc = dec = 1
            if root.left:
                if root.left.val == root.val + 1:
                    inc += left[0]
                elif root.left.val == root.val - 1:
                    dec += left[1]
            if root.right:
                if root.right.val == root.val + 1:
                    inc = max(inc, right[0] + 1)
                elif root.right.val == root.val - 1:
                    dec = max(dec, right[1] + 1)
            self.res = max(self.res, inc + dec - 1)
            return (inc, dec)
        dfs(root)
        return self.res