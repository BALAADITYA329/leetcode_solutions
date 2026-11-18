class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        i=j=0
        while i<len(s) and j<len(g):
            if g[j]<=s[i]:
                j+=1
            i+=1
        return j