class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                cur = stack.pop()
                if i == ')':
                    if cur != '(':
                        return False
                if i == ']':
                    if cur != '[':
                        return False
                if i == '}':
                    if cur != '{':
                        return False
        if len(stack) == 0:  return True
        else: return False