# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root,res)
        return res
    def helper(self, node, res):
        if node == None:
            return
        res.append(node.val)
        if node.left != None:
            self.helper(node.left, res)
        if node.right != None:
            self.helper(node.right, res)