import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __str__(self):
        return f'>> Vector({self.x}, {self.y}) <<'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, rhs):
        return Vector(self.x + rhs.x, self.y + rhs.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


def main():
    v1 = Vector(3, 4)
    print("v1", v1, abs(v1), bool(v1))
    v2 = Vector(2, 3)
    print("v2", v2, abs(v2), bool(v2))
    v3 = v1 + v2
    print("v3", v3, abs(v3), bool(v3))
    v4 = v1 * 10
    print("v4", v4, abs(v4), bool(v4))
    print(repr(v1), str(v1))


if __name__ == "__main__":
    main()
