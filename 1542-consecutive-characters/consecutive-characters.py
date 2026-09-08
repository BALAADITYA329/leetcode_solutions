class Solution:
    def maxPower(self, s: str) -> int:
        max_len=1
        cur_len=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cur_len+=1
            else:
                cur_len=1
            max_len=max(max_len,cur_len)
        return max_len