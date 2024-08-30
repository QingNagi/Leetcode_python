class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        se1, se2 = set(nums1), set(nums2)
        return [list(se1 - se2), list(se2 - se1)]