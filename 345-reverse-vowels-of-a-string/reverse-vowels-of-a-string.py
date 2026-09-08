class Solution:
    def reverseVowels(self, s: str) -> str:
        ans=list(s)
        l=0
        r=len(ans)-1
        li="AEIOUaeiou"
        while l<r:
            while l<r and ans[l] not in li:
                l+=1
            while l<r and ans[r] not in li:
                r-=1
            ans[l],ans[r]=ans[r],ans[l]
            l+=1
            r-=1
        return "".join(ans)