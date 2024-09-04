class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root and not root.left and not root.right:return [root.val]
        Left, Bottom, Right = [], [], []
        def dfsLeft(root):
            if root and (root.left or root.right):
                Left.append(root.val)
                if root.left: dfsLeft(root.left)
                else:  dfsLeft(root.right)
        def dfsBottom(root):
            if root:
                dfsBottom(root.left)
                dfsBottom(root.right)
                if not root.left and not root.right:
                    Bottom.append(root.val)
        def dfsRight(root):
            if root and (root.left or root.right):
                Right.append(root.val)
                if root.right: dfsRight(root.right)
                else: dfsRight(root.left)
        dfsLeft(root.left)
        dfsBottom(root)
        dfsRight(root.right)
        return [root.val] + Left + Bottom + Right[::-1]