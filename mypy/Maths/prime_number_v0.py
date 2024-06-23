def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for num in range(2, number):
        if not number % num:
            return False

    return True


for n in range(100):
    if is_prime(n):
        print(n)
