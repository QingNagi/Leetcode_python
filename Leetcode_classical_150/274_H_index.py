class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1: return 1 if citations[0] != 0 else 0
        temp =0
        citations.sort()
        n = len(citations)
        for i, y in enumerate(citations):
            if n - i > y: temp = y
            if y >= (n - i): return max(n - i, temp)
        return temp