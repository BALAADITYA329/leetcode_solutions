class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [(1, [0] * k) for _ in range(4 * n)]
        def make_node(value):
            p = value % k
            cnt = [0] * k
            cnt[p] = 1
            return [p, cnt]
        def merge(a, b):
            ap, ac = a
            bp, bc = b
            cnt = [0] * k
            for r in range(k):
                cnt[r] += ac[r]
            for r in range(k):
                nr = (ap * r) % k
                cnt[nr] += bc[r]
            prod = (ap * bp) % k
            return [prod, cnt]
        def build(node, l, r):
            if l == r:
                tree[node] = make_node(nums[l])
                return
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )
        def update(node, l, r, pos, value):
            if l == r:
                tree[node] = make_node(value)
                return
            mid = (l + r) // 2
            if pos <= mid:
                update(node * 2, l, mid, pos, value)
            else:
                update(node * 2 + 1, mid + 1, r, pos, value)
            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )
        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]
            mid = (l + r) // 2
            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)
            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)
            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)
            return merge(left, right)
        build(1, 0, n - 1)
        ans = []
        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)
            res = query(1, 0, n - 1, start, n - 1)
            ans.append(res[1][x])
        return ans