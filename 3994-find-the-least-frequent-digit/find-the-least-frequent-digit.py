class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        dic={}
        while n>0:
            d=n%10
            if d in dic:
                dic[d]+=1
            else:
                dic[d]=1
            n//=10
        return min(dic,key=lambda x: (dic[x],x))