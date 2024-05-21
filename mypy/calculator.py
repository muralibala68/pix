def main():
    for number in range(5):
        print(f"Square of {number} is", square(number))


def square(value: int) -> int:
    return value * value


if __name__ == "__main__":
    main()
