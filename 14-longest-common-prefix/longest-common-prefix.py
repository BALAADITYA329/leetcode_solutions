class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        fi=strs[0]
        last=strs[-1]
        min_len=min(len(fi),len(last))
        for i in range(min_len):
            if fi[i]!=last[i]:
                return fi[:i]
        return fi[:min_len]
