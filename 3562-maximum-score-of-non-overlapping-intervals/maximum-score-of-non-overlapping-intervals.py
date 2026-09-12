from bisect import bisect_right
from functools import lru_cache
class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))
        arr.sort()
        starts = [x[0] for x in arr]
        nxt = [0] * n
        for i in range(n):
            r = arr[i][1]
            nxt[i] = bisect_right(starts, r)
        @lru_cache(None)
        def dp(i, k):
            if i >= n or k == 0:
                return (0, ())
            score1, indices1 = dp(i + 1, k)
            score2, indices2 = dp(nxt[i], k - 1)
            score2 += arr[i][2]
            indices2 = tuple(sorted(
                indices2 + (arr[i][3],)
            ))
            if score2 > score1:
                return (score2, indices2)
            if score2 < score1:
                return (score1, indices1)
            return (score1, min(indices1, indices2))
        return list(dp(0, 4)[1])