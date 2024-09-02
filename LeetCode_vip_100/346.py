class MovingAverage:
    def __init__(self, size: int):
        self.stack = deque()
        self.n = size
        self.sum_all = 0
    def next(self, val: int) -> float:
        if len(self.stack) == self.n:
            cur = self.stack.popleft()
            self.sum_all -= cur
        self.stack.append(val)
        self.sum_all += val 
        return self.sum_all / len(self.stack)