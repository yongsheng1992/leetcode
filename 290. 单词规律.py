"""
    290. 单词规律
    ------------
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        len_p = len(pattern)
        words = list(filter(lambda x: x != ' ', s.split(" ")))
        len_w = len(words)

        if len_p != len_w:
            return False

        counter_p = {}
        counter_w = {}
        for i in range(0, len_p):
            counter_p.setdefault(pattern[i], [])
            counter_p[pattern[i]].append(i)
            w = words[i]
            counter_w.setdefault(w, [])
            counter_w[w].append(i)

        if len(counter_p) != len(counter_w):
            return False

        for i in range(0, len_p):
            char = pattern[i]
            w = words[i]

            if counter_p[char] != counter_w[w]:
                return False

        return True
