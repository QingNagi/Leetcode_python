# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.res = 0
        def dfs(root):
            if not root: return 0, 0
            l_sum, l_num = dfs(root.left)
            r_sum, r_num = dfs(root.right)
            cur_sum = l_sum + r_sum + root.val
            cur_num = l_num + r_num + 1
            self.res = max(self.res, cur_sum/cur_num)
            return cur_sum, cur_num
        dfs(root)
        return self.res