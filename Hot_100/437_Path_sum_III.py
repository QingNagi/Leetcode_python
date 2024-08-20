# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        def dfs(node: Optional[TreeNode], s: int) -> None:
            if node is None: return
            nonlocal ans
            s += node.val
            ans += cnt[s - targetSum]
            cnt[s] += 1
            print(cnt)
            dfs(node.left, s)
            dfs(node.right, s)
            cnt[s] -= 1  
        dfs(root, 0)
        return ans