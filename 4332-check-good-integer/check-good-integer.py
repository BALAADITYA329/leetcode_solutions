class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        summ=0
        sq_sum=0
        while n!=0:
            summ+=n%10
            sq_sum+=pow(n%10,2)
            n//=10
        return (sq_sum-summ)>=50