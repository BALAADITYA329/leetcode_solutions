class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=0
        n=len(nums)
        for i in range(k):
            s+=nums[i]
        a=s/k
        for i in range(k,n):
            s+=nums[i]-nums[i-k]
            a=max(a,s/k)
        return a