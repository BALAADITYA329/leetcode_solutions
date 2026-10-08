class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(st):
            count = 0

            for ch in st:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                if count < 0:
                    return False

            return count == 0

        level = {s}

        while level:
            result = []

            for st in level:
                if isValid(st):
                    result.append(st)

            if result:
                return result

            next_level = set()

            for st in level:
                for i in range(len(st)):
                    if st[i] not in '()':
                        continue

                    new_st = st[:i] + st[i + 1:]
                    next_level.add(new_st)

            level = next_level

        return [""]
        