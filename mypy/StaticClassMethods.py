class Util:

    @staticmethod
    def increment(x: int) -> int:
        return x + 1

    @staticmethod
    def decrement(x: int) -> int:
        return x - 1

def main():
    print(Util.increment(10))
    print(Util.decrement(10))


if __name__ == "__main__":
    main()