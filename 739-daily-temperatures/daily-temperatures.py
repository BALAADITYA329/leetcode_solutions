class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        ans=[0]*n
        stack=[]
        for i in range(n):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                index=stack.pop()
                ans[index]=i-index
            stack.append(i)
        return ans