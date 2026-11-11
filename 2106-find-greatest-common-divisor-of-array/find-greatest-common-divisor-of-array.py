class Solution:
    def findGCD(self, nums: list[int]) -> int:
        mn=min(nums)
        mx=max(nums)
        while mx%mn!=0:
            mn,mx=mx%mn,mn
        return mn