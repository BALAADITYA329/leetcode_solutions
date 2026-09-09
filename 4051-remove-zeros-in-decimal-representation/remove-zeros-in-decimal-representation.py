class Solution:
    def removeZeros(self, n: int) -> int:
        s=str(n)
        li=[]
        for i in s:
            if i!='0':
                li.append(i)
        return int("".join(li))