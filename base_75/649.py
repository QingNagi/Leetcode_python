class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        j, ban_d, ban_r = 0, 0, 0
        res = deque(senate)
        while len(res) > 1:
            n = len(res)
            while n > 0:
                i = res.popleft()
                if i == 'R' and ban_r == 0: 
                    ban_d += 1
                    res.append(i)
                elif i =='D' and ban_d == 0:
                    ban_r += 1
                    res.append(i)
                elif i =='R' and ban_r != 0:  ban_r -= 1
                elif i =='D' and ban_d != 0:  ban_d -= 1
                n -= 1
            if ban_d > len(res): return 'Radiant'
            elif ban_r > len(res): return 'Dire'
        return 'Radiant' if res[0] == 'R' else 'Dire'
