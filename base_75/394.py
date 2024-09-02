class Solution:
    def decodeString(self, s: str) -> str:
        stack, n, i = [], len(s), len(s)-1
        while i >= 0:
            if s[i].isalpha(): stack.append(s[i])
            elif s[i] == ']':  stack.append(s[i])
            elif s[i] == '[':
                k = 0
                i -= 1
                temp_n = 0
                i_n = 0
                while  i >= 0 and s[i].isdigit():
                    num = int(s[i]) * pow(10, i_n) + temp_n
                    i_n += 1
                    temp_n = num
                    i -= 1
                i += 1
                temp = ''
                while stack[-1] != ']':
                    cur = stack.pop()
                    temp += cur
                stack.pop()
                stack.append(temp*num)
            i -= 1
        stack.reverse()
        return ''.join(stack)