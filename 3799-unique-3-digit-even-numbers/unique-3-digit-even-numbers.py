class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans=0
        for i in range(100,1000,2):
            s1=str(i)
            if all(str(digits).count(c)>=s1.count(c) for c in set(s1)):
                ans+=1
        return ans