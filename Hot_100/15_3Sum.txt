class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = list()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            mid = i + 1
            r = n - 1
            rarget = -nums[i]
            if nums[mid] + nums[mid+1] > rarget or nums[r] + nums[r-1] < rarget :
                continue

            while mid < r:
                if mid > i+1 and nums[mid] == nums[mid-1]:
                    mid += 1
                    continue
                if r < n - 1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                if nums[r] + nums[mid]  == rarget:
                    res.append([nums[i] ,nums[mid] ,nums[r]])
                    mid += 1
                elif nums[r] + nums[mid]  > rarget:
                    r -= 1
                else:
                    mid += 1
        return res