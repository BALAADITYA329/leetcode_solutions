class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        ans=0
        cur_floor=0
        for r in requests:
            ans+=abs(r-cur_floor)
            cur_floor=r
        return ans
            