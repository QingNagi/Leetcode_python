class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mode_list = defaultdict(list)
        for s in strings:
            if s[0] == 'a':
                mode_list[s].append(s)
            else:
                tmp = list(s)                       #转化成一种模式 从'a****'
                for i in range(len(s)):
                    tmp[i] = chr( (ord(tmp[i]) - ord(s[0]) + 26) % 26 + ord('a') )
                tmp = ''.join(tmp)
                mode_list[tmp].append(s)
        res = []
        for mode, sublist in mode_list.items():
            res.append(sublist)               
        return res