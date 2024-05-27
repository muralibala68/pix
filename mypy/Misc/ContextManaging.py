class Employee:
    def __init__(self, name, age):
        if name is None or len(name.strip()) == 0:
            raise Exception("name is invalid")
        if age <= 0 or age > 100:
            raise Exception("age is invalid")
        self.name = name.strip()
        self.age = age
        self.active = True
        print("Object constructed")

    def __enter__(self):
        print("Context management: entering With block...")
        return self

    def __exit__(self, exc_type, exc_val, exc_trace_back):
        print("Context management: exiting With block and releasing the resources...")
        if exc_type:
            print(f"An exception occurred: {exc_val}")
            return False # propagating the exception, if any

    def __repr__(self) -> str:
        return f'Employee({self.name!r}, {self.age!r})'

    def __str__(self) -> str:
        return "Employee: [" + self.name + "][" + str(self.age) + "]"

    def __bool__(self) -> bool:
        return self.active


def main():
    try:
        with Employee("Murali", 62) as emp1:
            print(repr(Employee))
            print(repr(emp1))
            print(emp1)
            print(emp1.name)
            print(emp1.age)
            print(emp1.name, "Employed" if bool(emp1) else "Quit")

        #with Employee("Neeela", 100) as emp2:
        #    print(emp2.to_string())
    except Exception as e:
        print("Exception occurred ", e)


if __name__ == "__main__":
    main()
