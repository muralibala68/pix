class BankAccount:
    def __init__(self, name: str, balance: float) -> None:
        self.account_name = name
        self.account_balance = balance

    # Strange that getters must be defined before setters!!!
    @property
    def account_name(self) -> str:
        return self._name

    @property
    def account_balance(self) -> float:
        return self._balance

    @account_name.setter
    def account_name(self, value: str) -> None:
        if not value:
            raise ValueError("invalid name")
        self._name = value

    @account_balance.setter
    def account_balance(self, value: float) -> None:
        if value < 0:
            raise ValueError("invalid balance")
        self._balance = value

    def __str__(self) -> str:
        return f"{self.account_name}'s account balance is {self.account_balance}"


def main():
    account = BankAccount("Murali", float(0))
    print(account)
    account.account_name = "BalaMurali"
    print(account)
    account.account_balance = 123.45
    print(account)


if __name__ == "__main__":
    main()
