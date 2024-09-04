# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if root == None: return 0
        if self.isBST(root, -inf, inf) == True: return self.cnt(root)
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))
    def isBST(self, root: TreeNode, L: int, R: int) -> bool:  
        if root == None:
            return True
        if root.val <= L or R <= root.val:
            return False
        return self.isBST(root.left, L, root.val) and self.isBST(root.right, root.val, R)
    def cnt(self, root: TreeNode) -> int:       #统计树的结点个数
        if root == None:
            return 0
        return self.cnt(root.left) + self.cnt(root.right) + 1