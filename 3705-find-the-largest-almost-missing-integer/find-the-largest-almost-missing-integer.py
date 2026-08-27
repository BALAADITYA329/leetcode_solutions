class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k==1:
            dic={}
            ans=-1
            for i in nums:
                if i in dic:
                    dic[i]+=1
                else:
                    dic[i]=1
            for i in dic:
                if dic[i]==1:
                    ans=max(ans,i)
            return ans
        elif k==n:
            return max(nums)
        else:
            c0 = 0
            cn=0
            for x in nums:
                if x==nums[0]:
                    c0+=1
                if x==nums[n-1]:
                    cn+=1
            candidates=[]
            if c0==1:
                candidates.append(nums[0])
            if cn==1:
                candidates.append(nums[n-1])
            return max(candidates) if candidates else -1
        