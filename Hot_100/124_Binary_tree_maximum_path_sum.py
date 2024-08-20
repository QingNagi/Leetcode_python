# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_res = -inf
        def dfs(node):
            if not node: return 0
            nonlocal max_res
            l_val = dfs(node.left)
            r_val = dfs(node.right)
            max_res= max(max_res, l_val + r_val + node.val)
            return max(max(l_val, r_val) + node.val, 0)
        dfs(root)
        return max_res