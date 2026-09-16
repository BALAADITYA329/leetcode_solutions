class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod=10**9+7
        return math.comb(n+k-1,2*k)%mod