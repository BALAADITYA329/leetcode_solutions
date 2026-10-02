class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res=[]
        def valid(open_n,close_n,path):
            if open_n==0 and close_n==0:
                res.append("".join(path))
                return 
            if open_n>0:
                path.append('(')
                valid(open_n-1,close_n,path)
                path.pop()
            if close_n>open_n:
                path.append(')')
                valid(open_n,close_n-1,path)
                path.pop()
        valid(n,n,[])
        return res