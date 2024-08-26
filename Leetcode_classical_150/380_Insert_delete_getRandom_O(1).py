class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.idx_map = dict()
    def insert(self, val: int) -> bool:
        if val not in self.idx_map:
            self.idx_map[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False
    def remove(self, val: int) -> bool:
        if val in self.idx_map:
            swap_val, idx = self.nums[-1], self.idx_map[val]
            self.nums[idx] = swap_val
            self.idx_map[swap_val] = idx
            del self.idx_map[val]
            self.nums.pop()
            return True
        return False
    def getRandom(self) -> int:
        return choice(self.nums)