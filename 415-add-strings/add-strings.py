class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i=len(num1)-1
        j=len(num2)-1
        c=0
        li=[]
        while i>=0 or j>=0 or c:
            d1=ord(num1[i])-ord("0") if i>=0 else 0
            d2=ord(num2[j])-ord("0") if j>=0 else 0
            total=d1+d2+c
            c=total//10
            r=total%10
            li.append(str(r))
            i-=1
            j-=1
        return "".join(li[::-1])