class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = dict()
        for str1 in strs:
            temp = "".join(sorted(str1))
            memo[temp] = memo.get(temp, []) + [str1]
        return list(memo.values())