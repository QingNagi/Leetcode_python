class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1: return nums2
        if not nums2: return nums1
        i, j = 0, 0
        while i < m:
            if nums1[i] <= nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                nums2.sort()
        else:
            j = 0
            while i < len(nums1):
                nums1[i] = nums2[j]
                i += 1
                j += 1