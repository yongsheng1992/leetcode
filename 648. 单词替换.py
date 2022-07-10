from typing import List


class Node:

    def __init__(self, value: str = None, is_leaf: bool = False):
        self.value = value
        self.children = dict()
        self.is_leaf = is_leaf


class TrieTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]

        node.value = word
        node.is_leaf = True

    def walk(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
            if node.is_leaf:
                return node.value

        return None


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = TrieTree()
        for root in dictionary:
            trie.insert(root)
        ans = []

        for word in sentence.split(" "):
            root = trie.walk(word)
            if root is None:
                ans.append(word)
            else:
                ans.append(root)

        return " ".join(ans)


if __name__ == "__main__":
    solution = Solution()
    print(solution.replaceWords(dictionary=["cat", "bat", "rat"], sentence="the cattle was rattled by the battery"))
    print(solution.replaceWords(dictionary=["a", "b", "c"], sentence="aadsfasf absbs bbab cadsfafs"))
