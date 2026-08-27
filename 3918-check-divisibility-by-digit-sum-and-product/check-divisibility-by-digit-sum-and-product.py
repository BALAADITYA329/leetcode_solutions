class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ=0
        product=1
        temp=n
        while n!=0:
            summ+=n%10
            product*=n%10
            n//=10
        return temp%(summ+product)==0