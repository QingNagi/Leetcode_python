class Solution:
    def findPermutation(self, s: str) -> List[int]:
        if not s:
            return [1]
        res = [1]
        last_index_of_i = -1
        for index, ch in enumerate(s):
            if ch == 'I':
                res.append(index + 2)
                last_index_of_i = index
                continue
            if ch == 'D':
                res.insert(last_index_of_i + 1, index + 2)
        return res