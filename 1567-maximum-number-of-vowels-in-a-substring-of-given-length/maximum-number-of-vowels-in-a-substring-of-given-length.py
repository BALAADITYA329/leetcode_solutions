class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxl=0
        l=0
        r=k-1
        count_len=0
        li=['a','e','i','o','u']
        for i in range(k):
            if s[i] in li:
                count_len+=1
        maxl=max(maxl,count_len)
        while r<len(s)-1:
            if s[l] in li:
                count_len-=1
            l+=1
            r+=1
            if s[r] in li:
                count_len+=1
            maxl=max(maxl,count_len)
        return maxl
            