def factorial(n: int) -> int:
    return n * factorial(n-1) if n > 0 else 1

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))

# list comprehension
print([factorial(n) for n in range(5)])
# generator comprehension
print((factorial(n) for n in range(5)))

for x in (factorial(n) for n in range(5)):
    print(x)
