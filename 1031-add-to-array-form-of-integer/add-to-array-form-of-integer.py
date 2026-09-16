class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        i=len(num)-1
        ans=[]
        while i>=0 or k>0:
            if i>=0:
                k+=num[i]
                i-=1
            ans.append(k%10)
            k//=10
        return ans[::-1]