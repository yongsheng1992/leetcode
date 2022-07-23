class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self._size = size
        self._vals = []
        self._sum = 0


    def next(self, val: int) -> float:
        self._vals.append(val)
        self._sum += val
        if len(self._vals) > self._size:
            top = self._vals.pop(0)
            self._sum -= top

        return self._sum / len(self._vals)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

if __name__ == "__main__":
    mv = MovingAverage(3)
    print(mv.next(1))
    print(mv.next(10))
    print(mv.next(3))
    print(mv.next(5))