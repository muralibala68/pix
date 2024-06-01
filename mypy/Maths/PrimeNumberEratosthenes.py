def list_primes(limit: int) -> list[int]:
    # 0 and 1 are not prime
    if limit < 2:
        return []

    is_prime: list[bool] = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    print(is_prime)

    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            for multiple in range(number**number, limit + 1, number):
                is_prime[multiple] = False

    return [n for n in range(limit + 1) if is_prime[n]]


print(list_primes(10))
