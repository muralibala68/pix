from collections import namedtuple
from typing import List

Point = namedtuple('Point', ['x', 'y'])


def display_point(p: Point) -> None:
    print(f"{p} - {p.x},{p.y}")


def display_points(points: List[Point]) -> None:
    for point in points:
        display_point(point)


def main():
    p1: Point = Point(2,3)
    p2: Point = Point(2,3)
    p3: Point = Point(4,5)

    points: List[Point] = [p1, p2, p3]
    display_points(points)

    if p1 == p2:
        print(f"{p1} of {type(p1)} equals {p2} of {type(p2)}")

    p1_as_dict = p1._asdict()
    print(f"Point as dict: {p1_as_dict}, x is {p1_as_dict['x']}, y is {p1_as_dict['y']}")


if __name__ == "__main__":
    main()
