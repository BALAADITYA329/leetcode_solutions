class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
        def get_valid_substring(i):
            right = last[s[i]]
            j = i
            while j <= right:
                char = s[j]
                if first[char] < i:
                    return None
                right = max(right, last[char])
                j += 1
            return (i, right)
        intervals = []
        for char in first:
            interval = get_valid_substring(first[char])
            if interval:
                intervals.append(interval)
        intervals.sort(key=lambda x: (x[1], x[0]))  
        result = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end              
        return result