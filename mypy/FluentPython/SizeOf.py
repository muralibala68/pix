from sys import getsizeof

# Up to a range of 16, 'list comprehension' takes lesser memory than 'generator expression'
# This is because of the minimum overhead required for generator expression; that is 192 bytes in this case.
for x in range(50):
    print(x, "lc", getsizeof([n for n in range(x)]), "gc", getsizeof((n for n in range(x))))

type_names = {'int': 100,
              'float': 101.1,
              'str': 'xyz',
              'bool_True': True,
              'bool_False': False,
              'list': [],
              'dict': {},
              'tuple': ()}

# float takes 24 bytes while int takes more e.g. 28.
# This is because int has no fixed size memory like other languages.
# i.e., it can grow as needed and restricted by the physical memory
#
# surprisingly, even boolean takes 28 bytes ;) because it is implemented using int!
for type_name in type_names:
    print(type_name, type_names[type_name], getsizeof(type_names[type_name]))


# Beware, the following may take longer to complete
# so, remember to interrupt!!!
large_int = 0
try:
    while True:
        large_int += 1
        if not large_int % 100_000_000:
            print("largest int so far", large_int, getsizeof(large_int))
except MemoryError:
    print("Memory size exceeded!")
finally:
    print("largest int", large_int)
    print("largest int size", getsizeof(large_int))

