class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for z in tokens:
            if z.isdigit() or (len(z) > 1 and z[1:].isdigit): 
                nums.append(int(z))
            else: 
                y = nums.pop()
                x = nums.pop()
                temp = self.calc(x, y, z)    
                nums.append(temp)
        return nums[-1]
    def calc(self, x, y, z) -> int:
        if z == '+':   
            return x + y
        elif z == '*': 
            return x * y
        elif z == '-': 
            return x - y
        elif z == '/': 
            if x/y < 0: 
                return ceil(x / y)
            else: 
                return floor(x / y)