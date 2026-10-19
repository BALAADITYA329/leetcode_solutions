class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        li=sorted(nums)
        ans=[]
        for i in range(len(li)):
            if li[i]==target:
                ans.append(i)
        return ans