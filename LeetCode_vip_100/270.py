# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.distance, self.res = inf, inf
        def dfs(root):
            if not root: return
            dfs(root.left)
            dfs(root.right)
            temp = abs(target - root.val)
            if self.distance > temp:
                self.distance = temp
                self.res = root.val
            elif self.distance == temp:
                self.distance = temp
                self.res = min(root.val, self.res)
        dfs(root)
        return self.res