"""
    925. 长按键入
    ------------
    简单题目。使用递归也可以做。
"""
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j, l1, l2 = 0, 0, len(name), len(typed)

        while i < l1 and j < l2:
            if name[i] != typed[j]:
                return False

            c1 = 1
            while i + 1 < l1 and name[i] == name[i+1]:
                i += 1
                c1 += 1

            c2 = 1
            while j + 1 < l2 and typed[j] == typed[j+1]:
                j += 1
                c2 += 1

            i += 1
            j += 1

            if c1 > c2:
                return False

        if i == l1 and j == l2:
            return True

        return False
