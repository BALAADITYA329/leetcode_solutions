class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<=k:
            return s[::-1]
        else:
            v="r"
            s1=""
            for j in range(0,len(s),k):
                if v=='r':
                    d=s[j:j+k]
                    s1+=d[::-1]
                    v='n'
                else:
                    s1+=s[j:j+k]
                    v='r'
            return s1
