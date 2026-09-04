class Solution:
    def isHappy(self, n: int) -> bool:
        ans=set()
        while n!=0 and n not in ans:
            ans.add(n)
            t_sum=0
            while n>0:
                d=n%10
                t_sum+=d**2
                n //=10
            n=t_sum
        return n==1