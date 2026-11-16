class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            new=[]
            for i in range(0,len(s),k):
                group=s[i:i+k]
                digit_sum=sum(int(digit) for digit in group)
                new.append(str(digit_sum))
            s=''.join(new)
        return s