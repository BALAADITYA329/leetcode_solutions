class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        right = -1
        count = 0
        intervals = []
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    intervals.append((l, r))
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    intervals.append((l, r))
                l -= 1
                r += 1
        intervals.sort(key=lambda x: x[1])
        count = 0
        last_end = -1
        for l, r in intervals:
            if l > last_end:
                count += 1
                last_end = r       
        return count