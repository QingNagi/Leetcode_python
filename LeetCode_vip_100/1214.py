# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        memo = defaultdict(int)
        def dfs(root2):
            if not root2: return
            dfs(root2.left)
            memo[root2.val] += 1
            dfs(root2.right)
        dfs(root2)
        stack = []
        while root1 or len(stack) > 0:
            if root1: 
                stack.append(root1)
                root1 = root1.left
            else: 
                root1 = stack.pop()
                if target - root1.val in memo: return True
                root1 = root1.right
        return False