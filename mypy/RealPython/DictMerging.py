# While merging, overwrites duplicates, if any, from left to right
def merge_dict(d1: {}, d2: {}) -> {}:
    d3 = {**d1, **d2}
    print(f"merging {d1} and {d2} results in {d3}")


def main():
    d1 = {"one": 1, "two": 2}
    d2 = {"three": 3, "two": 2}
    d3 = merge_dict(d1, d2)


if __name__ == "__main__":
    main()
