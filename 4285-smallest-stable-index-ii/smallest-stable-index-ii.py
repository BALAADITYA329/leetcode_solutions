class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        p_max=[0]*n
        cur_max=-1
        for i in range(n):
            cur_max=max(cur_max,nums[i])
            p_max[i]=cur_max
        s_min=[0]*n
        cur_min=float('inf')
        for i in range(n- 1,-1,-1):
            cur_min=min(cur_min,nums[i])
            s_min[i]=cur_min
        for i in range(n):
            if p_max[i]-s_min[i]<=k:
                return i
        return -1