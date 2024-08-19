# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        self.helper(root, stack)
        print(stack)
        return stack[k-1]

    def helper(self, node, stack):
        if not node: return
        self.helper(node.left, stack)
        stack.append(node.val)
        self.helper(node.right, stack)