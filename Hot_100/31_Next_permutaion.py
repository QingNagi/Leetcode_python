class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums)-1,0,-1):
            # 对应第3部，找到下标l的位置,这里 l == i-1
            if nums[i-1] < nums[i]:
                for j in range(len(nums)-1,i-1,-1):

                    if nums[j] > nums[i-1]:
                        nums[i-1],nums[j] = nums[j],nums[i-1]
                        break
                for j in range((len(nums)-i+1)//2):
                    nums[i+j],nums[len(nums)-1-j] = nums[len(nums)-1-j] ,nums[i+j]
                return nums
        nums.reverse()