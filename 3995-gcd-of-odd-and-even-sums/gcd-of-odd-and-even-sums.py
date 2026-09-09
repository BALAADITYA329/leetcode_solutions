class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        even_sum=0
        odd_sum=0
        for i in range(1,2*n+1):
            if i%2==0:
                even_sum+=i
            else:
                odd_sum+=i
        return gcd(even_sum,odd_sum)