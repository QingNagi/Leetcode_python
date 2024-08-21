class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        list1 = []
        length = len(s)
        if len(s) <= 1:
            return list([[s]])
        def backtracking(i, index):
            if i == length:
                res.append(list1.copy())
                return
            if i < length -1:
                backtracking(i+1, index)
            t = s[index:i+1]
            if t == t[::-1]:
                list1.append(t)
                backtracking(i+1, i+1)
                list1.pop()
            
        backtracking(0, 0)
        return res