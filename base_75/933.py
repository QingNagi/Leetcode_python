class RecentCounter:
    def __init__(self):
        self.stack = []
        self.res = 0
        self.i = 0
    def ping(self, t: int) -> int:
        self.stack.append(t)
        if t - self.stack[self.i] <= 3000:
            self.res += 1
        else:
            self.res += 1
            while t - self.stack[self.i] > 3000:
                self.res -= 1
                self.i += 1
        return self.res