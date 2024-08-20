# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root in (None, p, q):
            return root
        res = []
        def dfs(node,res):
            if not node: return
            dfs(node.left, res)
            res.append(node.val)
            dfs(node.right,res)
        dfs(root, res)
        memo = dict()
        for i in range(len(res)):
            memo[res[i]] = i
        while True:
            if root.val in (None,q.val, p.val):
                return root
            if (memo[q.val] - memo[root.val]) * (memo[p.val] - memo[root.val]) < 0:
                return root
            elif memo[q.val] - memo[root.val] > 0:
                root = root.right
            elif memo[q.val] - memo[root.val] < 0:
                root = root.left