from dataclasses import dataclass


@dataclass(frozen=True)
class ImmutableClass:
    name: str
    value: int

    def to_string(self):
        return f"[{self.name}][{self.value}]"


def main():
    i1 = ImmutableClass("immutableInstance-1", 10)
    print(i1.to_string())


#    try:
#        i1.name = "xyz"
#    except Exception as e:
#        print(e)

if __name__ == "__main__":
    main()
