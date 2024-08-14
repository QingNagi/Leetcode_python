# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root == None:
            return 0 
        res = 0
        q = deque()
        q.append(root)
        while (len(q)) > 0:
            n = len(q)
            while n > 0:
                cur = q.popleft()
                if low <= cur.val <= high:
                    res += cur.val
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
                n -= 1
        return res        