class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 1 or sum > num * 9:
            return ""
        ans = []
        for i in range(num):
            remaining_positions = num - 1 - i
            cur = min(9, sum - remaining_positions * 0) 
            low = max(0, sum - remaining_positions * 9)
            high = min(9, sum)
            cur = min(9, sum)
            cur = max(0, sum - remaining_positions * 9)
            cur = min(9, max(cur, 0)) 
            cur = min(9, sum - (0)) 
            cur = min(9, sum)
            if sum - cur > remaining_positions * 9:
                cur = sum - remaining_positions * 9
            ans.append(str(cur))
            sum -= cur
        return "".join(ans)