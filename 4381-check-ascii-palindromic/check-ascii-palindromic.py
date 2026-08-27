class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary_char=[]
        for c in s:
            val=ord(c)
            for i in range(7,-1,-1):
                bit=(val>>i)&1
                binary_char.append(str(bit))
        binary_str="".join(binary_char)
        return binary_str==binary_str[::-1]