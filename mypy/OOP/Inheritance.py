class Shape:
    count_of_shapes_ = 0  # class variable

    @classmethod
    def count_of_shapes(cls):
        return cls.count_of_shapes_

    @classmethod
    def increment_count_of_shapes(cls):
        cls.count_of_shapes_ += 1

    def __init__(self, name: str):
        self.name = name
        Shape.increment_count_of_shapes()

    def __str__(self):
        return f"It is me; {self.name}"

    def name(self):
        return self.name

    def draw(self):
        print(self)


class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        self.instance_id = Shape.count_of_shapes()
        self.radius = radius

    def __str__(self):
        return f"It's me; {self.instance_id}: {self.name} of radius {self.radius}"

    def draw(self):
        print(self)

    def radius(self):
        return self.radius


def main():
    circle = Circle(5.0)
    circle.draw()

    print(Circle.count_of_shapes())
    print(Shape.count_of_shapes())


if __name__ == "__main__":
    main()
