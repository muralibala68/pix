from typing import Set, FrozenSet


# Does the given word have unique letters?
def heterogram(word: str) -> bool:
    sw: Set = set(word)
    return len(sw) == len(word)


print(heterogram("murali"))
print(heterogram("bala"))

l: list[int] = [1, 2, 3, 4]
print("set constructed from a set literal", {1, 2, 3, 4})  # does not like {l} as it says un-hashable!
print("set constructed from a list", set(l))
print("set constructed from a str", set("word"))
print("set constructed from a generator expression", {chr(n) for n in range(97, 123)})
print("set constructed from a generator expression", set(chr(n) for n in range(97, 123)))
print("can't construct an empty set using set literal as it would be a dict!", {}, type({}))

s: set[int] = set(l)  # mutable set
print(s)
s.add(999)
print(s)
s.remove(999)
print(s)

i_s: frozenset[int] = frozenset(l)  # immutable set
# i_s.add(999) cannot do this
print(i_s, type(i_s))

print("15 in binary: ", bin(15))
print("15 in octal: ", oct(15))
print("15 in hexadecimal: ", hex(15))
