class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        li=[]
        m=1
        while n>0:
            d=n%10
            if d>0:
                li.append(d*m)
            n//=10
            m*=10
        return li[::-1]