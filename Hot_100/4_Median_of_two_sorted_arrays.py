class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_k_min(nums1, start1, end1, nums2, start2, end2, k):
            remain1 = end1 - start1 + 1
            remain2 = end2 - start2 + 1
            if remain1 == 0:
                return nums2[start2 + k - 1]
            if remain2 == 0:
                return nums1[start1 + k - 1]
            if k == 1:
                return min(nums1[start1], nums2[start2])
            i = start1 + min(remain1, k // 2) - 1
            j = start2 + min(remain2, k // 2) - 1
            if nums1[i] <= nums2[j]:
                return get_k_min(nums1, i+1, end1, nums2, start2, end2, k - (i - start1 + 1))
            else:
                return get_k_min(nums1, start1, end1, nums2, j+1, end2, k - (j - start2 + 1))

        m, n = len(nums1), len(nums2)
        mid1 = (m + n + 1) // 2
        mid2 = (m + n + 2) // 2
        a = get_k_min(nums1, 0, m-1, nums2, 0, n-1, mid1)
        b = get_k_min(nums1, 0, m-1, nums2, 0, n-1, mid2)
        return (a + b) / 2
