class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def dfs(root):
            if not root: return 0
            l, r = dfs(root.left),dfs(root.right)
            depth = max(l, r) + 1
            res[depth].append(root.val)
            return depth
        res  = defaultdict(list)
        dfs(root)
        return [v for v in res.values()]