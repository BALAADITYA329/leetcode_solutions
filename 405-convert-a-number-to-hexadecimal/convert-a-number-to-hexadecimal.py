class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        if num<0:
            num+=2**32
        hex_c="0123456789abcdef"
        res=[]
        while num>0:
            rem=num%16
            res.append(hex_c[rem])
            num//=16
        return "".join(res[::-1])