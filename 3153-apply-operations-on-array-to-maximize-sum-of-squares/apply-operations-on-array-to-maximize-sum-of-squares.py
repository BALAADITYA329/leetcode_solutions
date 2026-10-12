class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 64
        for num in nums:
            for b in range(64):
                if num & (1 << b):
                    count[b] += 1
        ans = 0
        for _ in range(k):
            num = 0
            for b in range(64):
                if count[b] > 0:
                    num |= (1 << b)
                    count[b] -= 1
            ans = (ans + num * num) % MOD
        return ans