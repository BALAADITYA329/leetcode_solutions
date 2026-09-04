class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1={}
        dic2={}
        for i in range(len(s)):
            c_s=s[i]
            c_t=t[i]
            if c_s in dic1 and dic1[c_s]!=c_t:
                return False
            if c_t in dic2 and dic2[c_t]!=c_s:
                return False
            dic1[c_s]=c_t
            dic2[c_t]=c_s
        return True