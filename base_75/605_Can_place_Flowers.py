class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1: return 1>=n if flowerbed[0] ==0 else 0>=n
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            res = 1
            flowerbed[0] = 1
        else: 
            res = 0
        for i in range(1, len(flowerbed)):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                if i < len(flowerbed) - 1 and flowerbed[i+1] == 0:
                    res += 1
                    flowerbed[i] = 1
                elif i == len(flowerbed) - 1: res += 1
        return res >= n