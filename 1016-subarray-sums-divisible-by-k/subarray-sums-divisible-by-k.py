class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        dic={0:1}
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            r=s%k
            if r<0:
                r+=k
            if r in dic:
                count+=dic[r]
                dic[r]+=1
            else:
                dic[r]=1
        return count