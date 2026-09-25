class Solution:
    def isValid(self, s: str) -> bool:
        li=[]
        for i in s:
            if i in "({[":
                li.append(i)
            else:
                if not li:
                    return False
                top=li.pop()
                if i==')' and top!='(':
                    return False
                if i==']' and top!='[':
                    return False
                if i=='}' and top!='{':
                    return False
        return len(li)==0