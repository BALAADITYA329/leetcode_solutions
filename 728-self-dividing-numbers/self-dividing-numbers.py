def self_div_numbers(n):
    s=str(n)
    for i in s:
        if i=='0' or n%int(i)!=0:
            return False
    return True
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        li=[]
        for i in range(left,right+1):
            if self_div_numbers(i):
                li.append(i)
        return li