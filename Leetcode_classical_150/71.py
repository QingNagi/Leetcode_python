class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path) == 1: return path
        stack, n, i = [], len(path), 0
        temp_i, temp_x = 0, 0
        while i < n:
            if path[i] == '/':
                while i < n and path[i] == '/':
                    i += 1
                i -= 1
                stack.append('/')
                if len(stack) > 2 and stack[-2] == '/': stack.pop()
            elif path[i] == '.':
                while i < n and path[i] == '.':
                    temp_i += 1
                    i += 1
                if temp_i == 1 and stack[-1] == '/':
                    if  i < n and path[i] != '/':
                        stack.append('.'*temp_i)
                        temp_i = 0
                        continue
                    while i < n and path[i] == '/':
                        i += 1
                    i -= 1
                elif temp_i == 2 and stack[-1] == '/' :
                    if  i < n and  path[i] != '/':
                        stack.append('.'*temp_i)
                        temp_i = 0
                        continue
                    stack.pop()
                    while stack and stack[-1] != '/':
                        stack.pop()
                    if len(stack) == 0: stack.append('/')
                    while i < n and path[i] == '/':
                        i += 1
                    i -= 1
                else:
                    stack.append('.'*temp_i)
                    i -= 1
                temp_i = 0
            else:   stack.append(path[i])
            i += 1
        if len(stack) > 1 and stack[-1] == '/': stack.pop()
        return ''.join(stack)