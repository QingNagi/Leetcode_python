from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root == None:
            return res
        self.dfs(root, res, 0)
        return res

    def dfs(self, node, res, level):
        if node == None:
            return
        if level > len(res) - 1:
            res.append([])
        res[level].append(node.val)
        if node.left != None:
            self.dfs(node.left, res, level+1)
        if node.right != None:
            self.dfs(node.right, res, level+1)