class Solution:
    def calculate(self, s: str) -> int:
        st = [1]    # 符号栈，存放每一层的符号，一个括号表示一层；最顶层的符号为+1
        sign = 1    # 值为1或-1，表示当前数的符号
        n = len(s)
        i = 0
        res = 0
        while i < n:
            if s[i].isdigit():
                # 如果为数字，生成数值
                number = 0
                while i < n and s[i].isdigit():
                    number = number * 10 + int(s[i])
                    i += 1
                # 累加和，真实数字等于符号乘以数值
                res += sign * number
            else:
                if s[i] == '+':
                    sign = st[-1]   # 加号，获取当前层的符号
                elif s[i] == '-':
                    sign = -st[-1]  # 减号，获取当前层的相反符号
                elif s[i] == '(':
                    st.append(sign) # 左括号，进入新一层，将当前层符号入栈
                elif s[i] == ')':
                    st.pop()        # 右括号，完成一层的运算，弹出这一层符号
                i +=1   # 索引右移
        return res