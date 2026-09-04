class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n=len(arr)
        count=0
        cur_sum=0
        for i in range(k):
            cur_sum+=arr[i]
        if cur_sum/k>=threshold:
            count+=1
        l=0
        r=k
        while r<n:
            cur_sum+=arr[r]
            cur_sum-=arr[l]
            if cur_sum/k>=threshold:
                count+=1
            l+=1
            r+=1
        return count