from typing import Union


def valid(value) -> bool:
    return isinstance(value, (float, int))


def add(val1: Union[float, int], val2: Union[float, int]) -> [float, int]:
    if not valid(val1):
        raise Exception(f"invalid input val1: {val1}")
    if not valid(val2):
        raise Exception(f"invalid input val2: {val2}")
    return val1 + val2


def main():
    try:
        val1 = input("Enter value1: ")
        val2 = input("Enter value2: ")
        result = add(float(val1), float(val2))
        print(f"Value1 {val1} + Value2 {val2} = {result}")
    except Exception as e:
        print("Exception occurred ", e)


def square(value: int) -> int:
    return value * value


if __name__ == "__main__":
    main()
