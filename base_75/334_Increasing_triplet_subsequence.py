class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = sys.maxsize     # 位置i之前的最小值
        second = sys.maxsize    # 位置i之前的，有比它小的值的值
        for num in nums:
            if num <= first:
                first = num     # 更新最小值
            elif num <= second:
                second = num    # 更新second
            else:
                return True     # num之前有依次小于它的两个值，找打递增序列
        return False