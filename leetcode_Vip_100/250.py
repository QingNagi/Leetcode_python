# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node):
            if not node:  return None
            if not node.left and not node.right:
                self.ans += 1
                return node.val
            left = dfs(node.left)
            right = dfs(node.right)
            if (left is None or left == node.val) and (right is None or right == node.val):
                self.ans += 1
                return node.val
            return inf
        dfs(root)
        return self.ans