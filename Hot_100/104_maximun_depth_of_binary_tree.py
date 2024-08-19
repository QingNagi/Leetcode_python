# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        deep = 0
        if root:
            q.append(root)
        else:
            return deep
        while len(q) > 0:
            n = len(q)
            deep += 1
            while n > 0:
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                n -= 1
        return deep
