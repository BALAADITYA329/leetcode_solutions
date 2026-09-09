class Solution:
    def maxProduct(self, n: int) -> int:
        s=str(n)
        li=[int(i) for i in s]
        li.sort()
        return li[-1]*li[-2]