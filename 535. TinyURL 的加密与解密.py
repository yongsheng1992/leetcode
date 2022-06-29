import string
import random

class Codec:
    BASE62 = string.digits + string.ascii_letters
    PREFIX = "https://leetcode.com/"

    def __init__(self):
        self.cache = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = "".join([random.choice(self.BASE62) for _ in range(6)])
        self.cache[key] = longUrl
        return self.PREFIX + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl.replace(self.PREFIX, "")
        return self.cache[key]


if __name__ == "__main__":
    codec = Codec()
    print(codec.encode("https://leetcode.com/problems/design-tinyurl"))
    print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))