class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        for i in s:
            if i in ('{', '[', '('):
                stack.append(i)
            elif i == '}':
                if stack and stack[-1] == '{': stack.pop()
                else: return False
            elif i == ']':
                if stack and stack[-1] == '[': stack.pop()
                else: return False
            elif i == ')':
                if stack and stack[-1] == '(': stack.pop()
                else: return False
        return True if len(stack) == 0 else False