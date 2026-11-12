class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        def lcm(a,b):
            return (a*b)//gcd(a,b)
        n=len(nums)
        max_len=0
        for i in range(n):
            cur_prod=nums[i]
            cur_gcd=nums[i]
            cur_lcm=nums[i]
            for j in range(i+1,n):
                cur_prod *= nums[j]
                cur_gcd = gcd(cur_gcd,nums[j])
                cur_lcm = lcm(cur_lcm,nums[j])
                if cur_prod>cur_lcm * cur_gcd:
                    break
                if cur_prod == cur_lcm*cur_gcd:
                    if j-i+1>max_len:
                        max_len=j-i+1
        return max(max_len,1)