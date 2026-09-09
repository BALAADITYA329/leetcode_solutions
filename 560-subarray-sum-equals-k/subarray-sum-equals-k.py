class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_nums={0:1}
        total=0
        count=0
        for n in nums:
            total+=n
            if total-k in sub_nums:
                count+=sub_nums[total-k]
            sub_nums[total] =1+sub_nums.get(total,0)
        return count