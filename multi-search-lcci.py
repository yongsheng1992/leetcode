from typing import List


class TrieNode:

    def __init__(self, val=None):
        self.val = val
        self.leaf = False
        self.children = {}
        self.next = None


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def walk(self, key, callback=None):
        root = self.root
        i = 0
        while i < len(key):
            code = ord(key[i]) - ord('a')
            if code not in root.children:
                break
            root = root.children[code]
            i += 1
        return i, root

    def insert(self, key, value=None):
        i, root = self.walk(key)

        while i < len(key):
            code = ord(key[i]) - ord('a')
            node = TrieNode()
            root.children[code] = node
            root = root.children[code]
            i += 1

        root.leaf = True
        root.val = value

    def search(self, key):
        i, root = self.walk(key)

        if i < len(key):
            return None

        return root.val


class AC:

    def __init__(self):
        self.trie = Trie()
        self.trie.root.next = self.trie.root

    def insert(self, key, value=None):
        self.trie.insert(key, value)

    def build(self):
        root = self.trie.root
        queue = [root]
        while queue:
            root = queue.pop(0)

            for code, node in root.children.items():
                if root == self.trie.root:
                    node.next = root
                else:
                    next = root.next

                    while code in next.children:
                        next = next.children[code]

                    node.next = next

                queue.append(node)

    def bfs(self):
        root = self.trie.root
        queue = [root]
        while queue:
            root = queue.pop(0)
            for code, node in root.children.items():
                queue.append(node)

    def match(self, key):
        pass


class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        ac = AC()
        for index, small in enumerate(smalls):
            ac.insert(small, index)
        ac.build()



if __name__ == '__main__':
    pass

