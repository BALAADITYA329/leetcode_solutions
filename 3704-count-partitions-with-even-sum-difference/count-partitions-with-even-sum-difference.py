class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        li=[]
        total=sum(nums)
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            li.append(s)
        s=0
        count=0
        for i in range(len(nums)-1):
            s+=nums[i]
            right=total-s
            if (s-right)%2==0:
                count+=1
        return count