class SegmentTree:
    def __init__(self, n, init_vals):
        self.n = n
        self.tree = [0] * (4 * n)
        self.build(1, 0, n - 1, init_vals)

    def build(self, node, start, end, init_vals):
        if start == end:
            self.tree[node] = init_vals[start]
            return
        mid = (start + end) // 2
        self.build(2 * node, start, mid, init_vals)
        self.build(2 * node + 1, mid + 1, end, init_vals)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(2 * node, start, mid, l, r) ^ self.query(2 * node + 1, mid + 1, end, l, r)


class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        import sys
        sys.setrecursionlimit(200000)
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        parent = [0] * n
        depth = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        
        def dfs1(u, p, d):
            parent[u] = p
            depth[u] = d
            size = 1
            max_sub = 0
            for v in adj[u]:
                if v != p:
                    sub_size = dfs1(v, u, d + 1)
                    size += sub_size
                    if sub_size > max_sub:
                        max_sub = sub_size
                        heavy[u] = v
            return size

        cur_pos = 0
        def dfs2(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            if heavy[u] != -1:
                dfs2(heavy[u], h)
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    dfs2(v, v)

        dfs1(0, -1, 0)
        dfs2(0, 0)
        
        init_vals = [0] * n
        for i in range(n):
            init_vals[pos[i]] = 1 << (ord(s[i]) - ord('a'))
            
        seg_tree = SegmentTree(n, init_vals)
        
        def query_path(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] > depth[head[v]]:
                    u, v = v, u
                res ^= seg_tree.query(1, 0, n - 1, pos[head[v]], pos[v])
                v = parent[head[v]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= seg_tree.query(1, 0, n - 1, pos[u], pos[v])
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_val = 1 << (ord(c) - ord('a'))
                seg_tree.update(1, 0, n - 1, pos[u], new_val)
            else:
                u = int(parts[1])
                v = int(parts[2])
                mask = query_path(u, v)
                # Check if at most one bit is set
                if (mask & (mask - 1)) == 0:
                    ans.append(True)
                else:
                    ans.append(False)
                    
        return ans