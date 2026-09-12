class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            rev=27-(ord(s[i])-ord('a')+1)
            ans+=(i+1)*rev
        return ans