class Solution:
    def reverseWords(self, s: [str]) -> None:
        i = 0
        for j in range(len(s)): # aT bT c
            if s[j] != ' ': continue
            self.reverse(s, i, j)
            i = j + 1
        self.reverse(s, i, len(s)) # aT bT cT
        self.reverse(s, 0, len(s)) # c b a
    def reverse(self, s, i, j):
        for k in range(i, (i + j) // 2):
            g = j - 1 - k + i
            s[k], s[g] = s[g], s[k]