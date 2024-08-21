class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else: return -1
        l, r = 0, len(nums) - 1
        index = -1
        while l < r:
            mid = l + ((r -l)>>1)
            if nums[mid] == target:
                index = mid
            if nums[mid] <= nums[-1] :
                r = mid
            else:
                l = mid + 1 
        rot = r - 1
        if rot == len(nums) - 1:
            rot = 0
        if target > nums[-1]:
            if index != -1:
                return index
            else:
                l, r = 0, rot
                while l < r:
                    mid = l + ((r -l)>>1)
                    if nums[mid] == target:
                        index = mid
                    if nums[mid] > target :
                        r = mid
                    else:
                        l = mid + 1
        elif target == nums[-1]:
            return len(nums) - 1
        else:
            if index != -1:
                return index
            else:
                l, r = rot, len(nums) - 1
                if l == r:
                    if nums[l] != target:
                        return -1
                    else: return l
                while l < r:
                    mid = l + ((r -l)>>1)
                    if nums[mid] == target:
                        index = mid
                    if nums[mid] > target:
                        r = mid
                    else:
                        l = mid + 1
        return index if nums[l] != target else l