class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def dfs(root):
            nonlocal res
            if not root:return
            l,r=dfs(root.left),dfs(root.right)
            ans=1
            if root.left and root.left.val==root.val+1:
                ans=max(ans,l+1)
            if root.right and root.right.val==root.val+1:
                ans=max(ans,r+1)
            res=max(res,ans)
            return ans
        res=0
        dfs(root)
        return res