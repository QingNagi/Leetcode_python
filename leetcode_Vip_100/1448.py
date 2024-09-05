# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0 
        def dfs(node, ma):
            nonlocal cnt
            if not node: return
            if node.val >= ma:
                ma = node.val
                cnt += 1    
            dfs(node.left, ma)
            dfs(node.right, ma)
        dfs(root, -inf)
        return cnt