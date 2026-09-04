class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxm=0
        for i in nums:
            if i==1:
                count+=1
                maxm=max(count,maxm)
            else:
                count=0
        return maxm