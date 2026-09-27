class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            if i==')':
                cur_chs=[]
                while stack and stack[-1]!='(':
                    cur_chs.append(stack.pop())
                if stack and stack[-1]=='(':
                    stack.pop()
                for c in cur_chs:
                    stack.append(c)
            else:
                stack.append(i)
        return "".join(stack)