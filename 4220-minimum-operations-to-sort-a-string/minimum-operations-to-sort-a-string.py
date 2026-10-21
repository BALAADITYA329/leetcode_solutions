class Solution:
    def minOperations(self, s: str) -> int:
        if s=="".join(sorted(s)):
            return 0
        if len(s)==2:
            return -1
        n=len(s)
        min_char=min(s)
        max_char=max(s)
        if (s[0]==min_char) or (s[-1]==max_char):
            return 1
        if s[0]==max_char and s[-1]==min_char and s.count(min_char)==1 and s.count(max_char)==1:
            return 3
        return 2