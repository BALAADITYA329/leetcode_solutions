class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        ans = 0
        for k in range(1, n + 1):
            if n % k != 0:
                continue
            ok = True
            for start in range(0, n, k):
                end = start + k
                a = nums[start:end]
                b = target[start:end]
                if a == b:
                    continue
                drops = 0
                for j in range(k):
                    if a[j] > a[(j + 1) % k]:
                        drops += 1
                if drops != 1 or sorted(a) != b:
                    ok = False
                    break
            if ok:
                ans += k
        return ans