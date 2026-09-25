class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(i):
            result = set()
            current = {""}
            while i < len(expression) and expression[i] != '}':
                if expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1
                elif expression[i] == '{':
                    inside, i = parse(i + 1)
                    new_current = set()
                    for a in current:
                        for b in inside:
                            new_current.add(a + b)
                    current = new_current
                else:
                    new_current = set()
                    for a in current:
                        new_current.add(a + expression[i])
                    current = new_current
                    i += 1
            result |= current
            if i < len(expression) and expression[i] == '}':
                i += 1
            return result, i
        ans, _ = parse(0)
        return sorted(ans)