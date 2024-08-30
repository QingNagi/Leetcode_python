class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0] * len(nums1)
        memo = dict()
        for i, y in enumerate(nums1):
            if y not in memo:
                memo[y] = [i]
            else: memo[y] += [i]
        print(memo)
        for i, y in enumerate(nums2):
            res[memo[y][0]] = i
            memo[y].remove(memo[y][0])
        return res