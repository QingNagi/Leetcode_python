# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [-inf]
        self.helper(root, stack)
        if stack == sorted(stack):
            return True
        else: return False

    def helper(self, node, stack):
        if not node: return
        self.helper(node.left, stack)
        if stack[-1] < node.val:
            stack.append(node.val)
        else: 
            stack.append(-inf)
        self.helper(node.right, stack)