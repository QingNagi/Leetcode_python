class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res, strat = [], 0
        for i, y in enumerate(asteroids):
            if res and res[-1] * y < 0 and res[-1] > y:
                while res and res[-1] * y < 0:
                    if abs(res[-1]) == abs(y):
                        res.pop()
                        break
                    elif abs(res[-1]) < abs(y):
                        res.pop()
                    else: break
                else: res.append(y)
                continue
            res.append(y)
        return res