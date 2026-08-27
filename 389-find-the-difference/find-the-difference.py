class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d2={}
        for i in t:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        for i in d2:
            if i not in d or d2[i]>d[i]:
                return i
             
