class Solution:
    def countElements(self, arr: List[int]) -> int:
        if len(arr) == 1: return 0
        arr.sort()
        print(arr)
        res,temp = 0, 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1] + 1: 
                res += temp
                temp = 1
            if arr[i] == arr[i-1]: temp += 1
            else: temp = 1
        return res