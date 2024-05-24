
list1 = [1,2,3,4]
print("list1", list1)

list2 = [n for n in range(5)]
print("list2", list2)

# List comprehensions
#
squares = [n * n for n in range(5)]
print("squares_lc", squares)

even = [n for n in range(10) if not n % 2]
print("even_lc", even)

odd = [n for n in range(10) if n % 2]
print("odd_lc", odd)

# Generator comprehension
# Note: The main difference: here parenthesis '(' is used instead of square brackets '['
squares_gc = (n * n for n in range(5))
print("squares_gc", squares)
for n in squares_gc:
    print(n)
