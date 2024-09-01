class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 1: return [str(nums[0])]
        res = []
        s, i, n = '', 0, len(nums)
        while i < n - 1:
            s += str(nums[i])
            if nums[i] != nums[i+1] - 1:
                res.append(s)
                i += 1
                s = ''
                if  i < n and i == n-1: 
                    res.append(str(nums[i]))
                continue
            while i < n - 1 and nums[i] == nums[i+1] - 1:
                i += 1
            s += '->' + str(nums[i])
            res.append(s)
            s = ''
            i += 1
            if  i < n and i == n-1: 
                res.append(str(nums[i]))
        return res