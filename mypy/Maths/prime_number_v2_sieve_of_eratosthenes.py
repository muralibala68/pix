from math import sqrt


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number < 4:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    for n in range(5, int(sqrt(number)) + 1, 6):
        if number % n == 0 or number % (n + 2) == 0:
            return False
    return True


def test_negatives():
    for n in range(-1, -1000000, -1):
        assert not is_prime(n)


def test_zero():
    assert not is_prime(0)


def test_even():
    for n in range(4, 1000000, 2):
        assert not is_prime(n)


def test_multiple_of_3():
    for n in range(6, 1000000, 3):
        assert not is_prime(n)


def test_for_primes():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(11)
    assert is_prime(13)
    assert is_prime(17)
    assert is_prime(19)
    assert is_prime(23)
    assert is_prime(29)
    assert is_prime(31)
    assert is_prime(37)
    assert is_prime(41)
    assert is_prime(43)
    assert is_prime(47)
    assert is_prime(53)


def main():
    number = int(input('Number?'))
    result = 'not a prime'
    if is_prime(number):
        result = 'a prime'
    print(f'{number} is {result} number')


if __name__ == '__main__':
    main()

