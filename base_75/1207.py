class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        memo = Counter(arr)
        if len(set(memo.values())) == len(memo): return True
        else: return False