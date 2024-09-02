class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        priority = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}
        opt_stk = []
        num_stk = []
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
                continue
            elif s[i].isdigit() != 0:   #把当前这个数字找完
                num = int(s[i])
                while i+1 < n and s[i+1].isdigit() != 0:
                    num = num * 10 + int(s[i+1])
                    i += 1
                num_stk.append(num)
            elif s[i] == '(':
                opt_stk.append(s[i])
            elif s[i] == ')':           #把当前这个括号里的东西算完
                while opt_stk and opt_stk[-1] != '(':
                    opt = opt_stk.pop(-1)
                    y = num_stk.pop(-1)
                    x = num_stk.pop(-1)
                    z = self.calc(x, y, opt)
                    num_stk.append(z)
                opt_stk.pop()
            else :                      #是运算符号 加减之前，先把乘除计算完
                while opt_stk and priority[opt_stk[-1]] >= priority[s[i]]:
                    opt = opt_stk.pop(-1)
                    y = num_stk.pop(-1)
                    x = num_stk.pop(-1)
                    z = self.calc(x, y, opt)
                    num_stk.append(z)
                opt_stk.append(s[i])
            i += 1
        while opt_stk:              #收尾
            opt = opt_stk.pop(-1)
            y = num_stk.pop(-1)
            x = num_stk.pop(-1)
            z = self.calc(x, y, opt)
            num_stk.append(z)
        return num_stk[-1]
    def calc (self, x: int, y: int, opt: chr) -> int:
        if opt == '+':
            return x + y
        elif opt == '-':
            return x - y
        elif opt == '*':
            return x * y
        else:
            if x / y < 0:
                return ceil(x/y)
            else:
                return floor(x/y)