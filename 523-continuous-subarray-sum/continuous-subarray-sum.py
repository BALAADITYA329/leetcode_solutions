class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic={0:-1}
        ps=0
        for i in range(len(nums)):
            ps+=nums[i]
            r=ps%k
            if r in dic:
                if i-dic[r]>=2:
                    return True
            else:
                dic[r]=i
        return False            