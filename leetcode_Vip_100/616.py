class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        if not words:
            return s
        root = {}
        for word in words:
            # jy: 从 Trie 树的根节点将 word 插入;
            p = root
            for c in word:
                if c not in p:
                    p[c] = {}
                p = p[c]
            # jy: 经过以上循环后, p 为 word 的最后一个字符对应的子节点 {}, 在该
            #     子节点中加入 {"$": True} 表示该字符为一个单词的末尾;
            p['$'] = True
        _len = len(s)
        intervals = []
        # jy: 遍历字符串 s 中的每一个字符的下标;
        for i in range(_len):
            # jy: 从字符串 s 的下标为 i 的字符开始判断是否能构成某单词的前缀, 如果不能,
            #     则继续判断 s 字符串的下一个下标位置; 如果能, 则将相应的前缀的首末位置
            #     下标记录到区间列表 intervals 中(记录的过程会对区间进行去重处理);
            p = root
            j = i
            while j < _len and s[j] in p:
                p = p[s[j]]
                # jy: 如果 '$' 在当前节点 p 的子节点中, 表明当前节点 p 对应的字符的下标
                #     j 为止的部分(即 s[i: j+1] 存在于 words 中), 将首末下标位置 [i, j]
                #     添加到区间列表 intervals 中;
                if '$' in p:
                    # jy: 注意, 由于区间列表 intervals 中首末区间的末区间下标是前缀的最后
                    #     一个字符下标, 并非最后一个字符下标的下一个, 故判断是否要新增区间
                    #     时要确保新增区间的起始下标大于上一区间的末尾下标加 1 的结果, 因为
                    #     [1, 3] 和 [4, 6] 其实还是相邻的区间, 依然需要合并连接起来;
                    if not intervals or i > intervals[-1][1] + 1:
                        intervals.append([i, j])
                    elif j > intervals[-1][1]:
                        intervals[-1][1] = j
                j += 1
        # jy: 将 s 转换为字符列表, 随后在需要添加标签的首末下标区间的两侧对应的字符添加标签,
        #     最终将字符(部分已经是包含标签的子串)列表拼接为字符串;
        # jy: 也可以基于解法 2 中的思路对去重后的区间进行加标签;
        chars = list(s)
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            chars[start] = "<b>" + chars[start]
            chars[end] = chars[end] + "</b>"
        return "".join(chars)