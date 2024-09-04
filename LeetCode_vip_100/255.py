class Solution(object):
    def verifyPreorder(self, preorder):
        stack = []
        min_num = float("-inf")
        for i in range(len(preorder)):
            if preorder[i] < min_num: return False
            while stack and preorder[i] > stack[-1]:
                min_num = stack.pop()
            stack.append(preorder[i])
        return True