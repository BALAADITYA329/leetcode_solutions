class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result=[0]*k
        p=[0]*k
        for i in nums:
            c=[0]*k
            val=i%k
            c[val]+=1
            for j in range(k):
                if p[j]>0:
                    n=(j*val)%k
                    c[n]+=p[j]
            for r in range(k):
                result[r]+=c[r]
            p=c
        return result