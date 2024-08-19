from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = list([])
        if root == None:
            return res
        self.dfs(root, res, 0)
        print(res)
        return res

    def dfs(self, node, res, level):
        if level > len(res) - 1:
            res.append([])
        res[level].append(node.val)
        if node.left: self.dfs(node.left, res, level+1)
        if node.right: self.dfs(node.right, res, level+1)