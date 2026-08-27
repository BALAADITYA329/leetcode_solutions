class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n=1
        ans=0
        while n*k:
            if n*k in nums:
                pass
            else:
                ans=n*k
                break
            n+=1
        return ans