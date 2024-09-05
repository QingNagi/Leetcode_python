# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, leaf):
            if not root: return
            dfs(root.left, leaf)
            dfs(root.right, leaf)
            if not root.left and not root.right:
                leaf.append(root.val)
            return leaf
        leaf_1 = dfs(root1, [])
        leaf_2 = dfs(root2, [])
        return leaf_1 == leaf_2