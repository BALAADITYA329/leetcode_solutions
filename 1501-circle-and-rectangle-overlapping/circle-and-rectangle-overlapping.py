class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        c_x=max(x1,min(xCenter,x2))
        c_y=max(y1,min(yCenter,y2))
        d_x=xCenter-c_x
        d_y=yCenter-c_y
        return (d_x**2+d_y**2)<=(radius**2)