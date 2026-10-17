class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s
        n = len(nums)
        arr = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {v: i for i, v in enumerate(nums)}
        swaps = 0
        for i in range(n):
            if nums[i] != arr[i]:
                j = pos[arr[i]]
                pos[nums[i]] = j
                pos[arr[i]] = i
                nums[i], nums[j] = nums[j], nums[i]
                swaps += 1
        return swaps