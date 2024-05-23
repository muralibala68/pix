class Employee:
    def __init__(self, name, age):
        if name is None or len(name.strip()) == 0:
            raise Exception("name is invalid")
        if age <= 0 or age > 100:
            raise Exception("age is invalid")
        self.name = name.strip()
        self.age = age
        print("Object constructed")

    def __enter__(self):
        print("Context management: entering context...")
        return self

    def __exit__(self, exc_type, exc_val, exc_trace_back):
        print("Context management: exiting context and releasing the resources...")
        if exc_type:
            print(f"An exception occurred: {exc_val}")
            return False # propagating the exception, if any

    def to_string(self) -> str:
        return "Employee: [" + self.name + "][" + str(self.age) + "]"


def main():
    try:
        with Employee("Murali", 62) as emp1:
            print(emp1.to_string())
            print(emp1.name)
            print(emp1.age)

        #with Employee("Neeela", 100) as emp2:
        #    print(emp2.to_string())
    except Exception as e:
        print("Exception occurred ", e)


if __name__ == "__main__":
    main()