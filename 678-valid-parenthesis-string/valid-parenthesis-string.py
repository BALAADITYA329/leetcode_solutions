class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin=0
        cmax=0
        for ch in s:
            if ch=='(':
                cmin+=1
                cmax+=1
            elif ch ==')':
                cmin-=1
                cmax-=1
            else:
                cmin-=1
                cmax+=1
            if cmin<0:
                cmin=0
            if cmax<0:
                return False
        return cmin==0