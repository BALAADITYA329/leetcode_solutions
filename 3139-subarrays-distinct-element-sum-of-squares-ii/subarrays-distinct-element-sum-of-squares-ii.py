class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 1
        while size < n:
            size *= 2
        sum1 = [0] * (2 * size)
        sum2 = [0] * (2 * size)
        lazy = [0] * (2 * size)
        def update(node, start, end, l, r, val):
            if l > end or r < start:
                return
            if l <= start and end <= r:
                sum2[node] += 2 * val * sum1[node] + (end - start + 1) * val * val
                sum1[node] += (end - start + 1) * val
                lazy[node] += val
                return
            mid = (start + end) // 2
            push(node, start, end)
            update(node * 2, start, mid, l, r, val)
            update(node * 2 + 1, mid + 1, end, l, r, val)
            sum1[node] = sum1[node * 2] + sum1[node * 2 + 1]
            sum2[node] = sum2[node * 2] + sum2[node * 2 + 1]
        def push(node, start, end):
            if lazy[node] != 0 and start != end:
                mid = (start + end) // 2
                val = lazy[node]
                for child, length in (
                    (node * 2, mid - start + 1),
                    (node * 2 + 1, end - mid)
                ):
                    sum2[child] += 2 * val * sum1[child] + length * val * val
                    sum1[child] += length * val
                    lazy[child] += val
                lazy[node] = 0
        last = {}
        ans = 0
        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, size - 1, prev + 1, i, 1)
            last[x] = i
            ans = (ans + sum2[1]) % MOD
        return ans