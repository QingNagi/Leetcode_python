class Solution:
    def longestValidParentheses(self, s: str) -> int:
        a=[-1]
        ans=0
        for i in range(len(s)):
            if s[i]=='(':
                a.append(i)
            else:
                a.pop()
                if not a:
                    a.append(i)
                else:
                    ans=max(ans,i-a[-1])
        return ans