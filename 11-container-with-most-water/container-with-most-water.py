class Solution:
    def maxArea(self, height: list[int]) -> int:
        l=0
        r=len(height)-1
        best=0
        while l<r:
            h=min(height[l],height[r])
            w=r-l
            best=max(best,h*w)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return best