class Employee:
    def __init__(self, name, age):
        if name is None or len(name) == 0:
            raise Exception("name is invalid")
        if age <= 0 or age > 100:
            raise Exception("age is invalid")
        self.name = name
        self.age = age
        print("Object constructed")

    def __enter__(self):
        print("Context management: entering context (i.e., with block)...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Context management: exiting context (i.e., with block) and releasing the resources...")
        if exc_type:
            print(f"An exception occurred: {exc_val}")
            return False # propagating the exception, if any

    def __str__(self) -> str:
        return "Employee: [" + self.name + "][" + str(self.age) + "]"


def main():
    try:
        with Employee("Murali", 62) as emp1:
            print(emp1)
            print(emp1.name)
            print(emp1.age)

        #with Employee("Neeela", 100) as emp2:
        #    print(emp2.to_string())
    except Exception as e:
        print("Exception occurred ", e)


if __name__ == "__main__":
    main()
