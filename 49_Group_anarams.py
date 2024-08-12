class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        result = {}
        for s in strs:
            temp = ''.join(sorted(s))
            result[temp] = result.get(temp, []) + [s]
        return list(result.values())