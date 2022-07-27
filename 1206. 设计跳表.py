import random
import math
import sys


class SkipNode:

    def __init__(self, value, level, nxt=None):
        self.val = value
        self.level = level
        self.forwards = [nxt] * (level + 1)

    def forward(self):
        return [node.val for node in self.forwards if node is not None]


class Skiplist:

    MAX_LEVEL = 32

    def __init__(self):
        self.head = SkipNode(-sys.maxsize-1, self.MAX_LEVEL)
        self.level = 0

    def random_level(self, p=0.5):
        level = 1
        while random.random() < p and level < self.MAX_LEVEL:
            level += 1
        return level

    def search(self, target: int) -> bool:
        node = self.head
        for i in range(self.level, -1, -1):
            while node.forwards[i] and node.forwards[i].val < target:
                node = node.forwards[i]
            if node.forwards[i] and node.forwards[i].val == target:
                return True
        return False

    def add(self, num: int) -> None:
        node = self.head
        update = [None] * (self.MAX_LEVEL + 1)
        for i in range(self.level, -1, -1):
            while node.forwards[i] and node.forwards[i].val < num:
                node = node.forwards[i]
            update[i] = node

        lv = self.random_level()
        if lv > self.level:
            self.level += 1
            lv = self.level
            update[lv] = self.head

        new_node = SkipNode(num, lv)
        for i in range(lv+1):
            new_node.forwards[i] = update[i].forwards[i]
            update[i].forwards[i] = new_node

    def erase(self, num: int) -> bool:
        node = self.head
        update = [None] * (self.MAX_LEVEL + 1)
        for i in range(self.level, -1, -1):
            while node.forwards[i] and node.forwards[i].val < num:
                node = node.forwards[i]
            update[i] = node

        node = node.forwards[0]

        if node is None or node.val != num:
            return False

        for i in range(self.level + 1):
            if update[i].forwards[i] != node:
                break
            update[i].forwards[i] = node.forwards[i]

        if self.level > 0 and self.head.forwards[self.level] is None:
            self.level -= 1

        return True

    def print(self, level=0):
        node = self.head
        ans = []
        while node is not None:
            ans.append(node.val)
            node = node.forwards[level]
        print(ans)


if __name__ == "__main__":
    skip_list = Skiplist()
    ops = ["Skiplist","add","add","add","add","add","add","add","add","add","erase","search","add","erase","erase","erase","add","search","search","search","erase","search","add","add","add","erase","search","add","search","erase","search","search","erase","erase","add","erase","search","erase","erase","search","add","add","erase","erase","erase","add","erase","add","erase","erase","add","add","add","search","search","add","erase","search","add","add","search","add","search","erase","erase","search","search","erase","search","add","erase","search","erase","search","erase","erase","search","search","add","add","add","add","search","search","search","search","search","search","search","search","search"]
    nums = [[],[16],[5],[14],[13],[0],[3],[12],[9],[12],[3],[6],[7],[0],[1],[10],[5],[12],[7],[16],[7],[0],[9],[16],[3],[2],[17],[2],[17],[0],[9],[14],[1],[6],[1],[16],[9],[10],[9],[2],[3],[16],[15],[12],[7],[4],[3],[2],[1],[14],[13],[12],[3],[6],[17],[2],[3],[14],[11],[0],[13],[2],[1],[10],[17],[0],[5],[8],[9],[8],[11],[10],[11],[10],[9],[8],[15],[14],[1],[6],[17],[16],[13],[4],[5],[4],[17],[16],[7],[14],[1]]

    for idx, op in enumerate(ops):
        if idx == 0:
            continue
        if op == "add":
            skip_list.add(nums[idx][0])
        elif op == "erase":
            skip_list.erase(nums[idx][0])
