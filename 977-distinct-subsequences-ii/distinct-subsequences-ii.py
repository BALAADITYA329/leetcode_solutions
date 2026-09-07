class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod=10**9+7
        dp=[0]*26
        for char in s:
            idx=ord(char)-ord('a')
            total=sum(dp)%mod
            dp[idx]=(total+1)%mod
        return sum(dp)%mod