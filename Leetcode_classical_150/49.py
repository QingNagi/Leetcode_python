class Solution
    def groupAnagrams(self, strs List[str]) - List[List[str]]
        memo = defaultdict(list)
        for i in strs
            temp = ''.join(sorted(i))
            memo[temp].append(i)
        return list(memo.values())