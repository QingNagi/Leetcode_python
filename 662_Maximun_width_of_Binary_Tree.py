from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        q = deque()
        indexq = deque()
        res = 0
        q.append(root)
        indexq.append(1)

        while len(q) > 0:
            level = len(q)
            initialIndex = indexq[0]
            index = initialIndex
            while level > 0:
                cur = q.popleft()
                index = indexq.popleft()
                if cur is not None:
                    if cur.left is not None:
                        q.append(cur.left)
                        indexq.append(index*2)
                    if cur.right is not None:
                        q.append(cur.right)
                        indexq.append(index*2+1)
                level -= 1
                width = index - initialIndex + 1
                res = max(res, width)
        return res