class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        n, m = len(picture), len(picture[0])
        picture_t = list(zip(*picture))
        result = 0
        res = []
        for i in range(n):
            memo = Counter(picture[i])
            if memo['B'] == 1: 
                res.append(picture[i].index('B'))
        if len(res) == 0: return 0
        for i in res:
            memo = Counter(picture_t[i])
            if memo['B'] == 1: 
                result += 1
        return result