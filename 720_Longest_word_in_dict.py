class Solution:
    def longestWord(self, words: List[str]) -> str:
        if words == None or len(words) == 0:
            return ' '
        res = ''
        hashset = set()
        for word in words:
            hashset.add(word)
        for word in words:
            if len(word) > len(res) or (len(word) == len(res) and word < res):
                isword = True
                for i in range(0, len(word)):
                    if word[:i+1] not in hashset:
                        isword = False
                        break
                if (isword == True):
                    res = word
        return res
