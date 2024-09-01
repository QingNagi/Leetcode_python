class Solution:
    def parseTernary(self, expression: str) -> str:
        stack, i = [], len(expression) - 1
        while i >= 0:
            if expression[i] == '?':
                i -= 1 # expression[i] 为 "?" 时，expression[i - 1]就是条件 "T" or "F"
                cond = expression[i] # 获取条件"T" or "F"
                t = stack.pop() # 获取cond = "T"时的结果
                stack.pop() # pop掉 ":"
                f = stack.pop() # 获取cond = "F"时的结果
                if cond == 'T': # 做判断，把最终结果塞回 stack
                    stack.append(t)
                else:
                    stack.append(f)
            else: 
                stack.append(expression[i]) # 不是 "?"，统统塞进 stack
            i -= 1
        return stack[-1] # 最后只剩下最终结果在stack中