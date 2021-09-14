class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'}': '{', ')': '(', ']': '['}

        for p in s:
            if p in parentheses.keys():
                if not stack or parentheses[p] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(p)
        return True if not stack else False


# s = "{[()()]}{}"
# s = '[[[[]'
s = ']'
solution = Solution()
print(solution.isValid(s))
