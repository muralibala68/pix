balance: float = 0


def merge_dict(d1: {}, d2: {}) -> {}:
    d3 = {**d1, **d2}
    print(f"merging {d1} and {d2} results in {d3}")


def deposit(amount: float):
    global balance
    balance += amount
    print(f"balance after depositing {amount} is {balance}")


def withdraw(amount: float):
    global balance
    balance -= amount
    print(f"balance after withdrawing {amount} is {balance}")


def main():
    d1 = {"one": 1, "two": 2}
    d2 = {"three": 3, "two": 2}
    d3 = merge_dict(d1, d2)

    print()
    print(f"current balance is {balance}")
    deposit(100.43)
    withdraw(10.43)


if __name__ == "__main__":
    main()
