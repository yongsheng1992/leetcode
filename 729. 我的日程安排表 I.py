class MyCalendar:

    def __init__(self):
        self.dates = []

    def book(self, start: int, end: int) -> bool:
        for i, (s, e) in enumerate(self.dates):
            if start <= s < end:
                return False
            if start < e < end:
                print(2)
                return False
            if s <= start and e >= end:
                return False
            if start < s:
                self.dates.insert(i, (start, end))
                return True
            continue

        self.dates.append((start, end))
        return True


if __name__ == "__main__":
    calendar = MyCalendar()
    print(calendar.book(10, 20))
    print(calendar.book(15, 25))
    print(calendar.book(20, 30))
    print(calendar.book(0, 10))
    print(calendar.book())
    print(calendar.dates)