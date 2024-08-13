from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root == None:
            return res
        temp = deque()
        q = deque()
        q.append(root)
        while(len(q) > 0):
            n = len(q)
            list1 = []
            while n > 0:
                cur = q.popleft()
                list1.append(cur.val)
                if cur.left != None:
                    q.append(cur.left)
                if cur.right != None:
                    q.append(cur.right)
                n -= 1
            temp.appendleft(list1.copy())
            res = list(temp)
        return res