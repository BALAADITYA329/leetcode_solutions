class Solution:
    def calPoints(self, operations: list[str]) -> int:
        li=[]
        for i in operations:
            if i=='D':
                d=2*int(li[-1])
                li.append(d)
            elif i=='C':
                li.pop()
            elif i=='+':
                s=int(li[-1])+int(li[-2])
                li.append(s)
            else:
                li.append(int(i))
        return sum(li)
        

            