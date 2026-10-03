class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        li=[]
        for i in s:
            if li and i=='#':
                li.pop()
            elif i!='#':
                li.append(i)
        li1=[]
        for i in t:
            if li1 and i=='#':
                li1.pop()
            elif i!='#':
                li1.append(i)
        return li==li1
        