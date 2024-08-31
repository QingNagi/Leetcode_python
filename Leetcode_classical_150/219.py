class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res = defaultdict(int)
        for j in range(len(nums)):
            if j> k:
                del res[nums[j-k-1]]
            if nums[j] in res: return True
            res[nums[j]] = 0
            
        return False