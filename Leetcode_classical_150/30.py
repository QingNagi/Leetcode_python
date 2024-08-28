class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ls = len(s)         # 字符串s的长度
        m = len(words)      # 总单词数量
        n = len(words[0])   # 单个单词长度
        res = []
        if ls < m * n:
            return res      
        for i in range(n):
            diff = {}  
            for j in range(m):
                if i + (j + 1) * n > ls:    # 当前提取的子串单词右边界越界
                    break
                w = s[i + j * n : i + (j + 1) * n]
                diff[w] = diff.get(w, 0) + 1
            # 遍历words，进行做差
            for word in words:
                diff[word] = diff.get(word, 0) - 1
                if diff[word] == 0:
                    diff.pop(word)  
            for left in range(i, ls - m * n + 1, n):
                # 从第二个单词开始，开始要加入新单词，移除旧单词
                if left > i:
                    w = s[left + (m - 1) * n : left + m * n]    
                    diff[w] = diff.get(w, 0) + 1   
                    if diff[w] == 0:
                        diff.pop(w)
                    w = s[left - n : left]         
                    diff[w] = diff.get(w, 0) - 1    
                    if diff[w] == 0:
                        diff.pop(w)
                # diff为空，说明滑动窗口中的单词与word一致；left即为子串起点
                if not diff:
                    res.append(left)
        return res