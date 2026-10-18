class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        mod=10**9+7
        def helper(arr):
            if len(arr)<=2:
                return 1
            root=arr[0]
            left=[x for x in arr if x < root]
            right=[x for x in arr if x>root]
            ways_comb=math.comb(len(left)+len(right),len(left))%mod
            return (ways_comb* helper(left)*helper(right))%mod
        return (helper(nums)-1+mod)%mod