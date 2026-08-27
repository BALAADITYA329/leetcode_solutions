class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        k=0
        while i<len(s) and k<len(t):
            if s[i]==t[k]:
                i+=1
            k+=1
        return i==len(s)
