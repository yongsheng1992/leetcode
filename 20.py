"""
    20. 有效的括号
    -------------
    基本的简单题。
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char in {'(', '{', '['}:
                stack.append(char)
            else:
                if not stack:
                    return False
                m1 = mapping[char]
                m2 = stack.pop()
                if m1 != m2:
                    return False

        if stack:
            return False

        return True
