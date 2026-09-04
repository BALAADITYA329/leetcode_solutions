class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        s_min=[0]*n
        cur_min=float('inf')
        for i in range(n-1,-1,-1):
            cur_min=min(cur_min,nums[i])
            s_min[i]=cur_min
        cur_max=float('-inf')
        for i in range(n):
            cur_max=max(cur_max,nums[i])
            if cur_max- s_min[i]<=k:
                return i
        return -1