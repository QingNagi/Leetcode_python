class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        memo = Counter(word1)
        memo_2 = Counter(word2)
        res = []
        for i in memo.keys():
            if memo[i] != memo_2[i]:
                res.append(i)
            if i not in memo_2:
                return False
        if len(res) == 1: 
            if memo[res[0]] == memo_2[res[0]]:  return True
            else: return False
        temp_list = []
        for i in res:
            temp_list.append(memo_2[i])
        for i in res:
            if memo[i] in temp_list: 
                temp_list.remove(memo[i])
            else: 
                return False
        return True