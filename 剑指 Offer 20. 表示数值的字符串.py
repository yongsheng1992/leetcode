"""
    剑指 Offer 20. 表示数值的字符串
    -----------------------------
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        dot_flag = False
        e_flag = False
        num_flag = False

        for i in range(len(s)):
            char = s[i]

            if ord('0') <= ord(char) <= ord('9'):
                num_flag = True
            elif char == '.' and not e_flag and not dot_flag:
                dot_flag = True
            elif (char == 'e' or char == 'E') and not e_flag and num_flag:
                e_flag = True
                num_flag = False
            elif (char == '+' or char == '-') and (i == 0 or s[i-1] == 'e' or s[i-1] == 'E'):
                pass
            else:
                print(i, char)
                return False

        return num_flag
