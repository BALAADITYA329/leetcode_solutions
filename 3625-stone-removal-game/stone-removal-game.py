class Solution:
    def canAliceWin(self, n: int) -> bool:
        ans=10
        alice=True
        while n>=ans:
            n-=ans
            ans-=1
            alice=not alice
        return not alice