def factorial(n: int) -> int:
    return n * factorial(n - 1) if n > 0 else 1


print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))

# list comprehension
print([factorial(n) for n in range(5)])
# generator expression
ge = (factorial(n) for n in range(5))
print(ge)
for x in ge:
    print(x)

print("one by one(1)...")
ge = (factorial(n) for n in range(6))
while True:
    try:
        print(next(ge))
    except StopIteration:  # when you don't know the range
        break
print("done(1)")

print("one by one(2)...")
count = 6
ge = (factorial(n) for n in range(count))
for _ in range(count):
    print(next(ge))
print("done(2)")


def simple_generator():
    yield 1
    yield 2
    yield 3


for vv in simple_generator():
    print(vv)
