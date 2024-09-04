# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack, res = deque([root]), 0
        while len(stack) > 0:
            n = len(stack)
            res += 1
            while n > 0:
                root = stack.popleft()
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)
                n -= 1 
        return res