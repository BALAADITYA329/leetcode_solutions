class Solution:
    def removeDuplicates(self, s: str) -> str:
        li=[]
        for ch in s:
            if li and li[-1]==ch:
                li.pop()
            else:
                li.append(ch)
        return "".join(li)